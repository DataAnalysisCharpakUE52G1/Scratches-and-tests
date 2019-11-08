"""
Test script of the data

"""
from scratches.usefull import get_json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white")

head = get_json("exo/head.json")
data = pd.read_csv("exo/data1.csv")

ys: np.ndarray = data.values[:, 1:]
x: np.ndarray = np.arange(len(ys[0]))

print(ys.shape)

moy = np.array([y.mean() for y in ys])
plt.plot(moy, '+k')
plt.show()

ys = np.delete(ys, moy.argmax(), 0)
print(ys.shape)

prec = 0
end = 300
graph = sns.JointGrid(x, x)
for i, y in enumerate(ys[:end]):
    if int(100*i/end) != prec:
        prec = int(100*i/end)
        if prec < 10:
            print(f"0{prec}%")
        else:
            print(f"{prec}%")
    graph.y = y
    graph.plot_joint(plt.scatter, marker="+")
    graph.plot_marginals(sns.distplot)

plt.show()
