"""
Usefull functions
@date: 15/05/2019
@author: Quentin Lieumont
pulled from : https://github.com/QuentinN42/Stage_LRI/blob/master/useful/functions.py
LICENSE : GNU General Public License v3.0
"""
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import json


def get_json(link: str) -> dict:
    return json.load(open(link, "r"))


def write_json(link: str, data) -> None:
    _json = json.dumps(data, sort_keys=True, separators=(",", ": "))
    with open(link, "w") as f:
        for l in _json.split("\n"):
            f.write(l + "\n")


def idem_items(t: iter) -> bool:
    """
    :return: if all items are sames
    """
    return max(t) == min(t)


def same_len(vectors: iter) -> bool:
    """
    have all vectors the same length ?
    :param vectors: a list of Sized
    :return: if all vectors have the same length
    """
    lengths = list(map(len, vectors))
    return idem_items(lengths)


def readable(e) -> str:
    """
    format 0.15424548 in to 0.15
    :return: readable number
    """
    return str(int(e * 100) / 100)


def is_negative(n) -> int:
    if n < 0:
        return 1
    else:
        return 0


def shuffle(tab: iter) -> np.array:
    """
    shuffle an array
    :param tab: an array
    :return: the array with the same element but in different order
    """
    indices = np.arange(len(tab))
    np.random.shuffle(indices)
    return tab[indices]


def plot_3d(x: np.ndarray, y: np.ndarray, values: np.ndarray, labels: list = None) -> plt:
    """
    plot expected and result value over 2 axis
    :param x: x array
    :param y: y array
    :param values: z array
    :param labels: labels list
    :return: plt.Figure
    """
    fig = plt.figure()
    ax = Axes3D(fig)
    for val, lab in zip(values, labels):
        ax.plot(x, y, val, "o", label=lab)
    plt.legend()
    return fig
