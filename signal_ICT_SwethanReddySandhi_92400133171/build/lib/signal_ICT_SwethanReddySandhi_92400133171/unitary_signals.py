import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    
    n = np.asarray(n)
    signal = (n >= 0).astype(int)
    plt.stem(n, signal, use_line_collection=True)
    plt.title("Unit Step Signal u[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def unit_impulse(n):
 
    n = np.asarray(n)
    signal = (n == 0).astype(int)
    plt.stem(n, signal, use_line_collection=True)
    plt.title("Unit Impulse Signal δ[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def ramp_signal(n):
   
    n = np.asarray(n)
    signal = np.where(n >= 0, n, 0)
    plt.stem(n, signal, use_line_collection=True)
    plt.title("Ramp Signal r[n] = n·u[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal
