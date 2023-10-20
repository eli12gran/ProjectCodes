import numpy as np
import matplotlib.pyplot as plt


def externforcenumerical(gravity, F0, x0, mass, v0, w, gamma, longitude, plot=True):
    w0 = np.sqrt(g / l)

    # Formulas
    omega1 = np.sqrt(w0 ** 2 - (gamma ** 2) / 4)
    A = (F0 / m) / np.sqrt((w0 ** 2 - w ** 2) ** 2 + (gamma * w) ** 2)
    delta = np.arctan(gamma * w / (w0 ** 2 - w ** 2))
    beta = np.arctan((1 / omega1) * ((A * w * np.sin(delta)) / (x0 - A * np.cos(delta)) - gamma / 2))
    B = (x0 - A * np.cos(delta)) / np.cos(beta)

    time = np.arange(0, 60, 0.04)

    x = B * np.exp(-gamma * time / 2) * np.cos(omega1 * time + beta) + A * np.cos(w * time - delta)

    plt.plot(time, x)
    plt.grid("--")
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.title('Solution of the Differential Equation')
    plt.show()
