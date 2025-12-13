import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import keras
from keras.datasets import mnist
from keras import Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten

# Select the CPU and TensorFlow's backend.
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # commenta se vuoi usare la gpu
os.environ["KERAS_BACKEND"] = "tensorflow"


class Network():
    def __init__(self, model):
        self.model = model

    def feedforward(self, image):
        """Return the output of the network if "a" is input."""
        # aggiustiamo la shape dell'input
        print(f"The shape of the input is: {image.shape}.")
        image = image.reshape((1, 28, 28, 1)) # abbiamo un solo canale e una sola immagine da classificare
        print(f"The new shape of the image is: {image.shape}.")
        pred_image = self.model.predict(image)

        return pred_image

    # Questo sotto è un costruttore alternativo
    # In python a quanto pare si fa così
    # Nota che stiamo passando come parametro la classe stessa
    @classmethod
    def load(cls, filename: str):
        """Carica una rete usando keras (questo è solo un wrapper)"""
        loaded_model = keras.saving.load_model(filename)
        loaded_model.summary()
        model = cls(loaded_model) # creo una nuova istanza della classe
        return model
