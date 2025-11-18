import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import network
import mnist_loader
import matplotlib.pyplot as plt

class DrawingApp:
    def __init__(self, net):
        self.net = net

        self.window = tk.Tk()
        self.window.title("MNIST Digit Classifier")

        self.canvas_size = 280  # disegniamo su 280x280 e poi riduciamo a 28x28
        self.canvas = tk.Canvas(self.window, width=self.canvas_size, height=self.canvas_size, bg="black")
        self.canvas.pack()

        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "black")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.draw_event)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack()

        tk.Button(btn_frame, text="Classifica", command=self.classify).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Pulisci", command=self.clear).pack(side=tk.LEFT)

        self.window.mainloop()

    def draw_event(self, event):
        x, y = event.x, event.y
        r = 10
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill="white")

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.canvas_size, self.canvas_size], fill="black")

    def classify(self):
        x, arr = preprocess_for_mnist(self.image)

        # DEBUG: mostra cosa sta entrando nella rete
        # print("random value in the middle of x:", x[200:])
        print(x)
        plt.imshow(arr, cmap="gray")
        plt.show()

        out = self.net.feedforward(x)
        digit = np.argmax(out)

        print("\nRisultato:", digit)
        print("Output raw:", out.reshape(10))

def preprocess_for_mnist(img):
    # 1) Converti in scala di grigi
    img = img.convert("L")

    # 3) Binarizzazione leggera (togli rumore)
    img = img.point(lambda x: 0 if x < 30 else 255)

    # 4) Ritaglia la bounding box della cifra
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    # 5) Resize mantenendo proporzioni a max 20x20
    max_side = max(img.size)
    scale = 20.0 / max_side
    new_size = (max(1, int(img.size[0] * scale)),
                max(1, int(img.size[1] * scale)))
    img = img.resize(new_size, Image.Resampling.LANCZOS)

    # 6) Crea 28x28 nero e incolla al centro
    new_img = Image.new("L", (28, 28), 0)
    top_left = ((28 - new_size[0]) // 2, (28 - new_size[1]) // 2)
    new_img.paste(img, top_left)

    # 7) Converti in numpy + normalizza [0,1]
    arr = np.array(new_img).astype(np.float32) / 255.0

    # 8) reshape per la rete (784,1)
    return arr.reshape(784, 1), arr  # ritorno anche 28x28 per debug

if __name__ == "__main__":
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    net = network.Network.load("net.npz")
    app = DrawingApp(net)
