"""
Ce module permet de réaliser des Violin plot du jeux de données avec matplotlib.
"""

import sys
import matplotlib.pyplot as plt
import seaborn as sns


def violin_plot_iris(iris):
    """
    Méthode pour faire des violin plot (iris dataset).

    Parameter
    ---------
    iris: pandas dataframe
        le jeu de données à analyser
          - 4 attributs: sepal length & width et petal length & width
          - 3 classes: setosa, versicolour et virginica
          - 50 individus par classes
    """
    tmp = 1
    plt.figure(figsize=(15,10))

    for attribut in iris.columns[:-1]:
        plt.subplot(2, 2, tmp)
        ax = sns.violinplot(x="class", y=attribut, data=iris)
        tmp += 1

    plt.show()  # quand utilisé avec jupyther
    plt.clf()


def violin_plot_wdbc_global(wdbc):
    """
    Méthode pour faire des violinplot (wdbc dataset).

    Affichage de l'ensemble des paramètres du jeu de données sur un viloin plot
    unique.

    Permet de voir s'il y a ou non une disparité importante des données.

    Parameter
    ---------
    wdbc: pandas dataframe
        jeu de données wdbc - breast cancer
    """
    _, wdbc_col = wdbc.shape
    donnees = []

    for i in range(2, wdbc_col):
        donnees.append(wdbc.iloc[:,i].astype('float32'))

    fig, axs = plt.subplots(figsize=(8,5))
    axs.violinplot(dataset=donnees)
    axs.set_title("Affichage des paramètres du jeu de données")
    axs.set_label("Variables")
    axs.set_ylabel("Valeurs")

    plt.show()


def violin_plot_wdbc_specific(wdbc):
    """
    Méthode pour faire des violinplot de chaque paramètres (wdbc dataset).

    Parameter
    ---------
    wdbc: pandas dataframe
        jeu de données wdbc - breast cancer
    """
    rows, cols = (8,4)
    fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(15,25))
    tmp = 2

    for i in range(0, rows):
        for j in range(0, cols):
            if tmp < 32:
                sns.violinplot(x=wdbc[1], y=wdbc[tmp].astype('float32'),
                               ax=axs[i][j])
            tmp += 1

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sys.exit()  # Aucune action souhaitée
