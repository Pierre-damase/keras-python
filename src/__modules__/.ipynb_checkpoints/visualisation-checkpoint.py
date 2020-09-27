"""
Ce module permet de réaliser des Violin plot du jeux de données avec matplotlib.
"""

import sys
import matplotlib.pyplot as plt
import seaborn as sns


def violin_plot(iris):
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

    #name = "iris-violinplot"
    #plt.savefig(name, dpi=300)

    plt.show()  # quand utilisé avec jupyther
    plt.clf()
    

if __name__ == "__main__":
    sys.exit()  # Aucune action souhaitée
