"""
Ce proramme est une initiation à la conception d'un projet de machine learning.

Le jeu de données iris.data est utilisé.

Usage
-----
    conda activate deep-learning
    python iris.py
"""

import sys
from keras.models import Sequential
from keras.layers import Dense

from __modules__.data_file import read_data
from __modules__.visualisation import *


if __name__ == "__main__":
    iris = read_data()
    violin_plot(iris)

    # Input variables
    X = []
    for attribut in iris.columns[:-1]:
        X.append(iris[attribut])

    # Output variables
    Y = [0] * 50 + [1] * 50 + [2] * 50  # Class 0 - setosa,
                                        #       1 - versicolor
                                        #       2 - virginica

    """
    KERAS MODEL



    Dense class -> fully-connected network structure

      - The model expects rows of data with 4 variables - input_dim=4
      - The first hidden layer has 10 nodes and uses the sigmoid activat° funct°
      - The second hidden layer has 4 nodes and uses the sigmoid activat° funct°
      - The output layer has 3 node and uses the sigmoid activat° funct°

    Sigmoid on the output layer ensure that our network output is between 0 & 1.
    """

    # Define Keras Model
    model = Sequential()
    model.add(Dense(10, input_dim=4, activation="sigmoid"))
    model.add(Dense(4, activation="sigmoid"))
    model.add(Dense(3, activation="sigmoid"))

    # Compile Keras Model
