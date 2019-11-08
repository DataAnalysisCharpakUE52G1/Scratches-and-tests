"""
Fourier 1 signal
@date: 15/10/2019
@author: Quentin Lieumont, Nour Boulahcen
"""
import numpy as np
import matplotlib.pyplot as plt
from scratches.usefull import generate_signal


x = np.linspace(0, 10 * np.pi, 1000)
y = generate_signal(x, [1], [2 / np.pi])
# Get the fourier transform
# abs(complex) -> modulus
yf = abs(np.fft.rfft(y))


fig, ax = plt.subplots()

ax.plot(yf, "+k", label="fourier")

fig.legend()
fig.show()


f = yf.argmax() / 10
print(f, max(yf))
y2 = np.sin(2 * f * x)


fig, ax = plt.subplots()

ax.plot(y, label="in")
ax.plot(y2, label="out")

fig.legend()
fig.show()
