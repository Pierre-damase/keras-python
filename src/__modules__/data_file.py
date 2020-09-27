"""
Ce module lit le fichier iris.data situé dans le répertoire data.

Il permet de:
  - Lire le fichier iris.data
  - Vérifier l'existence du fichier iris.data
  - Renvoyer dans
"""

import os
import pandas as pd
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


def read_data(fichier, *args):
    """
    Méthode de lecture d'un fichier .data.

    Sauvegarde au format pandas DataFrame les données.

    Parameter
    ---------
    fichier: str

    args: tupple
        - 0: le nom des colonnes du DataFrame
        - 1: le type des données

    Return
    ------
    df: pandas DataFrame
        les données au format pandas DataFrame
    """
    path = "../data/"

    if valide_file(fichier, path):
        donnees = []
        with open(path + fichier, "r") as filin:
            for line in filin:
                if not line == "\n":
                    tmp = line.strip().split(',')
                    donnees.append(tmp)
            if args:
                df = pd.DataFrame(donnees, columns=args[0], dtype=args[1])
            else:
                df = pd.DataFrame(donnees)
            return df
    else:
        raise Exception("{} doit être présent dans le répertoire data/"
                        .format(fichier))


if __name__ == "__main__":
    sys.exit()  # Aucune action souhaitée si exécuté en tant que script
