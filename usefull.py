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
import json


def get_json(link: str) -> dict:
    return json.load(open(link, "r"))


def write_json(link: str, data) -> None:
    _json = json.dumps(data, sort_keys=True, separators=(",", ": "))
    with open(link, "w") as f:
        for l in _json.split("\n"):
            f.write(l + "\n")


def nmap(func: callable, l: np.ndarray) -> np.ndarray:
    """
    Map build-in function for numpy
    :param func: the function to map like f
    :param l: a list like [a, b, c] (or numpy array)
    :return: numpy.array(f(a), f(b), f(c))
    """
    return np.array(list(map(func, l)))


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


def shuffle(tab: iter) -> np.ndarray:
    """
    shuffle an array
    :param tab: an array
    :return: the array with the same element but in different order
    """
    indices = np.arange(len(tab))
    np.random.shuffle(indices)
    return tab[indices]


def generate_signal(x: np.ndarray, amps: list, freqs: list):
    signals: list = []
    for amp, freq in zip(amps, freqs):
        signals.append(amp * np.sin(2 * np.pi * freq * x))
    return sum(signals)


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


def plot_heat_map(
    z: iter, x: iter = None, y: iter = None, nb_ticks: int = 5, plot_title: str = ""
) -> plt:
    """
    plot a 2D colored graph of a 2D array
    :param z: the 2D array
    :param x: x axis label
    :param y: y axis label
    :param nb_ticks: number of labels over 1 axis
    :param plot_title: the plot title
    :return: plt.Figure
    """
    fig, ax = plt.subplots()
    im = ax.imshow(z)
    # ax.plot([len(z) - 0.5, -0.5], [-0.5, len(z) - 0.5], "-k")
    if plot_title is not "":
        ax.title._text = plot_title
    fig.tight_layout()
    fig.colorbar(im)
    if x is not None:
        if y is None:
            y = x
        ticks_pos_x = nmap(int, np.arange(nb_ticks) * (len(x) - 1) / (nb_ticks - 1))
        ticks_pos_y = nmap(int, np.arange(nb_ticks) * (len(y) - 1) / (nb_ticks - 1))
        ax.set_xticks(ticks_pos_x)
        ax.set_yticks(ticks_pos_y)
        ax.set_xticklabels([x[i] for i in ticks_pos_x])
        ax.set_yticklabels([y[i] for i in ticks_pos_y])
    return fig
