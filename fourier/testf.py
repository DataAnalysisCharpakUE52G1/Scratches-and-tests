import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

"""

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()
"""

"""
J'ai trouvé ca sur stack overflow ya aussi une doc pour scipy.fttpack : https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
Du coup sur le code qu'on avait ca nous donne ca :
"""

n = 600
X = np.linspace(0, 10 * np.pi, n)
y = []
t = 1.0 / 800000
A = [5, 2, 1 / 2, 1]
F = [1, 2, 4, 10]

for a, f in zip(A, F):
    y.append(a * np.sin(2 * np.pi * f * X))

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

yf2 = scipy.fftpack.fft(Y)
xf2 = np.linspace(0.0, 1.0 / t, int(n / 2))

fig, ax = plt.subplots()
ax.plot(xf2, 2.0 / n * np.abs(yf2[: n // 2]), "+k")
plt.show()
