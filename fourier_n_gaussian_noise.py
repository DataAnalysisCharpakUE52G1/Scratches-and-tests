import numpy as np
import matplotlib.pyplot as plt
from scratches.usefull import generate_signal, r_squared as r2
from scipy.integrate import trapz as integ

ech = 50
end = 5*np.pi
x = np.linspace(0, end, ech)

f_ins = [1]  #
a_ins = [1]  #
y = generate_signal(x, a_ins, f_ins)  # + np.random.normal(scale=0.005, size=len(x))
# y = np.array([1 if np.sin(X) >= 0 else -1 for X in x]) + np.random.normal(scale=2, size=len(x))

yf: np.ndarray = abs(np.fft.rfft(y))


def dif(_x, _ys, np_points: int = 1000):
    fig, ax = plt.subplots()

    for _y in _ys:
        ax.plot(_x[:np_points], _y[:np_points])

    fig.show()


def extract_coefs(signal: np.ndarray, nb: int = 1, act: int = None, plot: bool = True, graph_len: int = 200):
    fig, ax = plt.subplots()
    ax.plot(signal[:graph_len])
    if act is None:
        act = int(np.pi)
    freqs: list = []
    amps: list = []
    for n in range(nb):
        freqs.append(signal.argmax()/end)
        mi = int(signal.argmax() - act)
        if mi < 0:
            mi = 0
        ma = int(signal.argmax() + act)
        amps.append(integ(signal[mi:ma])/len(signal))
        signal[mi:ma] = np.zeros(ma - mi)
        if plot:
            ax.plot(signal[:graph_len])
    if plot:
        fig.show()
    return amps, freqs


a_out, f_out = extract_coefs(yf, 1, plot=True)

y2 = generate_signal(x, a_out, f_out)

dif(x, (y, y2), int(len(x)*2/end))
print(a_out)
print(r2(y, y2))

