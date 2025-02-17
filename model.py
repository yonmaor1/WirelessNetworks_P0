import numpy as np
import matplotlib.pyplot as plt

def los(d_lo, d_hi):
    # P_r = 25 + 20 log_10(0.125 / (4pi * d))

    d = np.linspace(d_lo, d_hi, 1000)
    P_r = 25 + 20 * np.log10(0.125 / (4 * np.pi * d))

    plt.plot(d, P_r)
    plt.xlabel('Distance (d)')
    plt.ylabel('Received Power (P_r)')
    plt.title('Received Power vs Distance')
    plt.grid(True)
    plt.show()

los(0, 6)