import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """Generate a unit step signal u[n] for integer index array n."""
    n = np.asarray(n)
    signal = (n >= 0).astype(int)
    plt.stem(n, signal)  # removed use_line_collection
    plt.title("Unit Step Signal u[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def unit_impulse(n):
    """Generate a unit impulse signal δ[n] for integer index array n."""
    n = np.asarray(n)
    signal = (n == 0).astype(int)
    plt.stem(n, signal)  # removed use_line_collection
    plt.title("Unit Impulse Signal δ[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def ramp_signal(n):
    """Generate a discrete-time ramp r[n] = n·u[n]."""
    n = np.asarray(n)
    signal = np.where(n >= 0, n, 0)
    plt.stem(n, signal)  # removed use_line_collection
    plt.title("Ramp Signal r[n] = n·u[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal
