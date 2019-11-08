"""
Test script of the data

"""
from scratches.usefull import get_json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white")

head = get_json("data/exo/head.json")
data = pd.read_csv("data/exo/data1.csv")

ys: np.ndarray = data.values[:, 1:]
x: np.ndarray = np.arange(len(ys[0]))

print(x[:10])
print(ys[0, :10])

graph = sns.JointGrid(x, x)

for y in ys[:2, :]:
    graph.y = y
    graph.plot_joint(plt.scatter, marker="+")
    graph.plot_marginals(sns.kdeplot, shade=True)

plt.show()
