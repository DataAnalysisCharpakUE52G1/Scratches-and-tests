import numpy as np
from matplotlib import pyplot as plt
from math import pi

X = np.linspace(0, 10 * pi, 2000)
y = []

A = [5, 2, 1/2, 1]
F = [1, 2, 4, 10]

for a, f in zip(A, F):
    y.append(a*np.sin(2*pi*f*X))


Y = sum(y)


fig: plt.Figure
fig, axs = plt.subplots(len(y))

for i, _y in enumerate(y):
    axs[i].plot(X, _y)

fig.show()


fig: plt.Figure
ax: plt.Axes
fig, ax = plt.subplots()

ax.plot(X, Y)

fig.show()
