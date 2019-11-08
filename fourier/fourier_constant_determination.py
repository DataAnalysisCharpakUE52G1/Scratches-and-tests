import numpy as np
import matplotlib.pyplot as plt
from scratches.usefull import generate_signal, r_squared as r2, fourier_constant as fc
from scipy.integrate import trapz as integ
from scipy import stats


ech = 100000
end = 5 * np.pi
x = np.linspace(0, end, ech)
f_ins = [1]


def extract_coefs(
    _x: np.ndarray,
    signal: np.ndarray,
    nb: int = 1,
    act: int = None,
    plot: bool = True,
    graph_len: int = 200,
):
    if plot:
        fig, ax = plt.subplots()
        ax.plot(signal[:graph_len], "+")
    if act is None:
        act = 1
    freqs: list = []
    amps: list = []
    for n in range(nb):
        freqs.append(signal.argmax() / end)
        mi = int(signal.argmax() - act)
        if mi < 0:
            mi = 0
        ma = int(signal.argmax() + act + 1)
        amps.append(integ(signal[mi:ma], _x[mi:ma]))
        signal[mi:ma] = np.zeros(ma - mi)
        if plot:
            ax.plot(signal[:graph_len])
    if plot:
        fig.show()
    return amps, freqs


prec = 1000
val = np.zeros((prec - 1, prec - 1))
ams = np.linspace(0, 20, prec)[1:]
frs = np.linspace(0, 20, prec)[1:]

for i in range(prec - 1):
    for j in range(prec - 1):
        y = generate_signal(x, [ams[i]], [frs[j]])
        yf: np.ndarray = abs(np.fft.rfft(y))
        a_out, f_out = extract_coefs(x, yf, 1, plot=False)
        val[i][j] = a_out[0]


f, a = plt.subplots()
a.plot(frs, val[2, :], "k+")
f.show()


# slope, intercept, r_value, p_value, std_err = stats.linregress(bli,bla)

# print(slope, std_err)
