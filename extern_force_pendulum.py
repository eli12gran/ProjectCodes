import numpy as np

def extern_force_numerical(fd_values, initial_theta, mass, omega, gamma, length):
    """
    :param fd_values: List of Extern Force Values
    :param initial_theta: Initial value for angle theta
    :param mass: Mass of the object
    :param omega: Initial value for extern force frequency
    :param gamma: Value of drag coefficient
    :param length: Length of the string
    :return:
    """
    gravity = 9.8
    time = np.arange(0, 60, 0.04)
    for FD in fd_values:
        omega = [omega]
        theta = [initial_theta]
        for i in range(len(time) - 1):
            omega.append(omega[i] - (gravity / length * np.sin(theta[i]) + gamma * omega[i] -
                                     (FD / mass) * np.cos(2 / 3 * time[i])) * time[1])
            theta.append(theta[i] + omega[i + 1] * time[1])
    return theta


extern_force_numerical([1.2], 0.2, 1, 0., 0.5, 4.)
