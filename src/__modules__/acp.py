"""
Ce module permet de réaliser une ACP avec python.
"""

import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd
from scipy.spatial import ConvexHull
import seaborn as sns
import sys


def pareto(data) :
    y = list(data)
    x = range(len(data))
    ycum = np.cumsum(y)/sum(y)*100
    fig, ax = plt.subplots()
    ax.bar(x,y,color="yellow")
    ax2 = ax.twinx()
    ax2.plot(x,ycum, color="C1", marker="D", ms=7)
    ax2.axhline(y=80,color="r")
    ax2.yaxis.set_major_formatter(PercentFormatter())
    ax.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")
    plt.ylim(0,110)
    plt.show()


def biplot(x=None,y=None,score=None,coeff=None,coeff_labels=None,
           score_labels=None,circle='T',bigdata=1000,cat=None,cmap="Set1",
           density=True):
    if score is not None : x = score
    if x.shape[1]>1 :
        xs = x[:,0]
        ys = x[:,1]
    else :
        xs = x
        ys = y
    if (len(xs) != len(ys)):
        print("Warning! x et y n'ont pas la même taille !")
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    #x_c = xs * scalex
    #y_c = ys * scaley
    temp = (xs - xs.min())
    x_c = temp / temp.max() * 2 - 1
    temp = (ys - ys.min())
    y_c = temp / temp.max() * 2 - 1
    print("Attention : pour des facilités d'affichage, "
          "les données sont centrées-réduites")
    if cat is None:
        cat = [0]*len(xs)
    elif len(pd.Series(cat)) == 1:
        cat = list(pd.Series(cat))*len(xs)
    elif len(pd.Series(cat)) != len(xs):
        print("Warning ! Nombre anormal de catégories !")
    cat = pd.Series(cat).astype("category")
    fig = plt.figure(figsize=(6,6),facecolor='w')
    ax = fig.add_subplot(111)
    # Affichage des points
    if (len(xs) < bigdata):
        ax.scatter(x_c,y_c, c = cat.cat.codes,cmap=cmap)
        if density==True:
            print("Warning ! Le mode density actif n'apparait que si BigData "
                  "est paramétré.")
    # Affichage des nappes convexes (BigData)
    else :
        #color
        norm = \
            mpl.colors.Normalize(vmin=0, vmax=(len(np.unique(cat.cat.codes))))
        #-(len(np.unique(c)))
        cmap = cmap
        m = cm.ScalarMappable(norm=norm, cmap=cmap)
        if density==True :
            sns.set_style("white")
            sns.kdeplot(x_c,y_c)
            sns.kdeplot(x_c,y_c, cmap="Blues", shade=True, shade_lowest=True, )
        #print(x_c)
        #print(y_c)
        for cat_temp in cat.cat.codes.unique() :
            x_c_temp = [
                x_c[i] for i in range(len(x_c)) if(cat.cat.codes[i] == cat_temp)
            ]
            y_c_temp = [
                y_c[i] for i in range(len(y_c)) if(cat.cat.codes[i] == cat_temp)
            ]
            points = [ [ None ] * len(x_c_temp) ] * 2
            points = np.array(points)
            points = points.reshape(len(x_c_temp),2)
            points[:,0] = x_c_temp
            points[:,1] = y_c_temp
            hull = ConvexHull(points)
            temp = 0
            for simplex in hull.simplices:
                color_temp = m.to_rgba(cat_temp)
                plt.plot(points[simplex, 0], points[simplex, 1],
                         color=color_temp)
                #, linestyle='dashed')#linewidth=2,color=cat)

                if (temp == 0) :
                     plt.xlim(-1,1)
                     plt.ylim(-1,1)
                     temp = temp+1
    if coeff is not None :
        if (circle == 'T') :
            x_circle = np.linspace(-1, 1, 100)
            y_circle = np.linspace(-1, 1, 100)
            X, Y = np.meshgrid(x_circle,y_circle)
            F = X**2 + Y**2 - 1.0
            #fig, ax = plt.subplots()
            plt.contour(X,Y,F,[0])
        n = coeff.shape[0]
        for i in range(n):
            plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5,
                      head_width=0.05, head_length=0.05)
            if coeff_labels is None:
                plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1),
                         color = 'g', ha = 'center', va = 'center')
            else:
                plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, coeff_labels[i],
                         color = 'g', ha = 'center', va = 'center')
        if score_labels is not None :
            for i in range(len(score_labels)) :
                temp_x = xs[i] * scalex
                temp_y = ys[i] * scaley
                plt.text(temp_x,temp_y,list(score_labels)[i])
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid(linestyle='--')
    #plt.show()


if __name__ == "__main__":
    sys.exit()  # Aucune action souhaitée
