"""
Ce module lit le fichier iris.data situé dans le répertoire data.

Il permet de:
  - Lire le fichier iris.data
  - Vérifier l'existence du fichier iris.data
  - Renvoyer dans
"""

import os
import pandas as pd
import numpy as np
import sys


def valide_file(fichier, path):
    """Vérifie que le fichier data est valide.

    I.E:
      - fichier présent dans le répertoire data/

    Parameter
    ---------
    fichier: str
        le nom du fichier data
    path: str
        le path du fichier data

    Return
    ------
    Boolean
      - True: fichier valide
      - False: fichier non valide
    """
    if os.path.exists(path + fichier):
        return True
    return False


def read_data():
    """
        
    """

def read_iris():
    """Lit le fichier iris.data.

    Return
    ------
    iris: pandas dataframe
        le jeu de données à analyser
    """
    fichier = "iris.data"
    path = "../data/"

    if valide_file(fichier, path):
        col_names = ['sepal_length', 'sepal_width', 'petal_length',
                     'petal_width', 'class']  # variables du dataset
        donnees = []

        with open(path + fichier, "r") as filin:
            for line in filin:
                if not line == "\n":
                    tmp = line.strip().split(',')
                    donnees.append(tmp)
            iris = pd.DataFrame(donnees, columns=col_names, dtype=float)
        return iris
    else:
        raise Exception("iris.data doit être présent dans le répertoire data/")


def read_wdbc():
    """Lit le fichier breast-cancer-wisconsin.data.

    Return
    ------
    cancer: pandas dataframe
        le jeu de données à analyser
    """
    fichier = "wdbc.data"
    path = "../data/"

    if valide_file(fichier, path):
        donnees = []

        with open(path + fichier, "r") as filin:
            for line in filin:
                if not line == "\n":
                    tmp = line.strip().split(',')
                    donnees.append(tmp)
            wdbc = pd.DataFrame(donnees)
        return wdbc
    else:
        raise Exception("iris.data doit être présent dans le répertoire data/")
        
        
if __name__ == "__main__":
    sys.exit()  # Aucune action souhaitée si exécuté en tant que script
