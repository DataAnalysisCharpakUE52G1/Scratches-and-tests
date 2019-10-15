import numpy as np
import matplotlib.pyplot as plt
from scratches.usefull import generate_signal


ech = 10000
f_ins = [2/np.pi, 3/np.pi]
a_ins = [1, 0.5]
x = np.linspace(0, 10*np.pi, ech)
y = generate_signal(x, a_ins, f_ins) + np.random.normal(scale=0.2, size=len(x))


yf: np.ndarray = abs(np.fft.rfft(y))


def extract_coefs(signal: np.ndarray, nb: int = 1, act: int = None, plot: bool = True):
    if plot:
        fig, ax = plt.subplots()
        ax.plot(signal[:50])
    if act is None:
        act = 5
    freqs: list = []
    amps: list = []
    for n in range(nb):
        freqs.append(signal.argmax()/10)
        amps.append(round(max(signal)/len(signal), 3))
        mi = int(signal.argmax() - act)
        if mi < 0:
            mi = 0
        ma = int(signal.argmax() + act)
        signal[mi:ma] = np.zeros(ma - mi)
        if plot:
            ax.plot(signal[:50])
    if plot:
        fig.show()
    return amps, freqs


a_out, f_out = extract_coefs(yf, 2, plot=False)
f_out = [f/np.pi for f in f_out]

y2 = generate_signal(x, a_out, f_out)


fig, ax = plt.subplots()

ax.plot(y[:1000], label="in")
ax.plot(y2[:1000], label="out")

fig.legend()
fig.show()
