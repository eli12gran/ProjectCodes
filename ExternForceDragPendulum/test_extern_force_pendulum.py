import numpy as np
from extern_force_pendulum import extern_force_numerical

def test_extern_force_pendulum():
    """
    :param force: Extern Force Value
    :param initial_theta: Initial value angle theta
    :param mass: Mass of the object
    :param omega: Extern Force frequency
    :param gamma: Coefficient Drag
    :param length: Longitude of string
    :return:
    """
    # Formulas
    force = 1.2
    initial_theta = 0.2
    mass = 1
    omega = 2/3
    gamma = 0.5
    length = 4
    gravity = 9.8
    omega0 = np.sqrt(gravity / length)
    omega1 = np.sqrt(omega0 ** 2 - (gamma ** 2) / 4)
    A = (force / mass) / np.sqrt((omega0 ** 2 - omega ** 2) ** 2 + (gamma * omega) ** 2)
    delta = np.arctan(gamma * omega / (omega0 ** 2 - omega ** 2))
    beta = np.arctan((1 / omega1) * ((A * omega * np.sin(delta)) /
                                     (initial_theta - A * np.cos(delta)) - gamma / 2))
    B = (initial_theta - A * np.cos(delta)) / np.cos(beta)

    # Time array
    time = np.arange(0, 60, 0.04)

    # List for keeping x values
    x = []
    for i in range(len(time)):
        x.append(B * np.exp(-gamma * time[i] / 2) * np.cos(omega1 * time[i] + beta) +
                 A * np.cos(omega * time[i] - delta))

    # Numeric method results
    numerical_solution = extern_force_numerical([force], initial_theta, mass, 0.0, gamma, length)

    difference = [abs(e1 - e2) for e1, e2 in zip(numerical_solution[0:1500], x[0:1500])]
    assert all(diff < 0.1 for diff in difference)
    return
