# plot for boundary layer, WKBJ, and Multiple scale methods


import numpy as np
import matplotlib.pyplot as plt


def BL_plot():
    epsilon = [0.25, 0.05, 0.1, 0.2]
    x = np.linspace(0, 1, 100)
    for i in range(4):
        y = (np.exp(x / epsilon[i]) - 1) / (np.exp(1 / epsilon[i]) - 1)
        t = epsilon[i]
        plt.plot(x, y, label="$\epsilon =$" + "%f" %t)

    plt.title("boundary layer")
    plt.xlabel("x")
    plt.legend(loc="upper right")
    plt.show()


def WKB_plot():
    epsilon = [0.25, 0.0001]
    x = np.linspace(0, 20, 100)
    for i in range(2):
        y = (np.sin(x / np.sqrt(epsilon[i])) / np.sin(1 / np.sqrt(epsilon[i])))
        t = epsilon[i]
        plt.plot(x, y, label="$\epsilon =$" + "%f" %t)

    plt.title("WKB")
    plt.xlabel("x")
    plt.legend(loc="upper right")
    plt.show()


def MS_plot():
    epsilon = 0.1
    t = np.linspace(0, 25, 100)
    # Exact solution
    term = epsilon / np.sqrt(1 - epsilon ** 2) * np.sin(np.sqrt(1 - epsilon ** 2) * t)
    y1 = np.exp(-epsilon * t) * (np.cos(np.sqrt(1 - epsilon ** 2) * t) + term)
    # two term expansion
    y2 = np.cos(t) + epsilon * (-t * np.cos(t) + np.sin(t))
    # One term multiple scales expansions
    y3 = np.exp(-t * epsilon) * np.cos(t)
    plt.plot(t, y1, label="exact solution")
    plt.plot(t, y2, label="two term expansion")
    plt.plot(t, y3, label="one term multiple scales expansion")
    plt.title("Multiple Scales Method")
    plt.xlabel("t")
    plt.legend(loc="upper right")
    plt.show()


