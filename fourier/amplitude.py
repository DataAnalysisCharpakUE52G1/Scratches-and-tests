import numpy as np
from scratches.usefull import plot_multiples
from scratches.fourier.fourier_n_gaussian_noise import extract_coefs

ech = 5000
end = 5 * np.pi
x = np.linspace(0, end, ech)


def test_amp(freq: float):
    global x
    y = np.sin(freq * x)
    yf: np.ndarray = abs(np.fft.rfft(y))

    a_out, f_out = extract_coefs(yf, 1, plot=False)
    return a_out


freqs = np.linspace(np.pi, 2 * np.pi, 10000)
res = np.array([test_amp(f) for f in freqs])
plot_multiples(freqs, [res])
