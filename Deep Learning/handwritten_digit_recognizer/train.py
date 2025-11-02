import numpy as np
import mnist_loader
import network
import matplotlib.pyplot as plt

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
x, y = training_data[13]
print("shape x:", x.shape)  # (784,1)
print("random value in the middle of x:", x[200:])
print("etichetta:", np.argmax(y))
img = x.reshape(28, 28)
plt.imshow(img, cmap="gray")
plt.show()

# net = network.Network([784, 30, 10])
# # net.SGD(training_data, 10, 10, 3.0)
# net.SGD(training_data, 10, 10, 3.0, test_data=test_data)
# net.save("net.npz")

