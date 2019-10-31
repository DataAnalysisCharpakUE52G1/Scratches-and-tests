import numpy as np
from scratches.usefull import plot_multiples, generate_signal
from scratches.fourier.fourier_n_gaussian_noise import extract_coefs
from matplotlib import pyplot as plt

ech = 5000
end = 5 * np.pi
x = np.linspace(0, end, ech)


y = np.sin(2 * np.pi * x + np.pi)
yf: np.ndarray = abs(np.fft.rfft(y))

a_out, f_out = extract_coefs(yf, 1, plot=True)
y_fit = generate_signal(x, a_out, f_out)
print(a_out, f_out)


fig: plt.Figure
ax: plt.Axes
fig, ax = plot_multiples(x, [y, y_fit], ["y", "y_fit"], nb_points=400)
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.show()
