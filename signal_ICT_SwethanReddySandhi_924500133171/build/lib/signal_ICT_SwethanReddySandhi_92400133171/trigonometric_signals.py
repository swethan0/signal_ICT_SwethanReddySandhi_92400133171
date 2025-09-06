"""
trigonometric_signals.py
Functions:
- sine_wave(A, f, phi, t)
- cosine_wave(A, f, phi, t)
- exponential_signal(A, a, t)

Each function returns (t, x) and plots using matplotlib.

t: numpy array of time instants (seconds)
f: frequency in Hz
phi: phase in radians
A: amplitude
a: exponent coefficient for exponential (x = A * exp(a*t))
"""

import numpy as np
import matplotlib.pyplot as plt

def _plot(t, x, title="Signal", xlabel="t (s)", ylabel="Amplitude"):
    plt.figure(figsize=(8,3))
    plt.plot(t, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def sine_wave(A, f, phi, t):
    """
    A: amplitude
    f: frequency in Hz
    phi: phase in radians
    t: numpy array of time instants
    """
    t = np.asarray(t)
    x = A * np.sin(2 * np.pi * f * t + phi)
    _plot(t, x, title=f"Sine wave: A={A}, f={f}Hz, phi={phi} rad")
    return t, x

def cosine_wave(A, f, phi, t):
    t = np.asarray(t)
    x = A * np.cos(2 * np.pi * f * t + phi)
    _plot(t, x, title=f"Cosine wave: A={A}, f={f}Hz, phi={phi} rad")
    return t, x

def exponential_signal(A, a, t):
    """
    x(t) = A * exp(a * t)
    """
    t = np.asarray(t)
    x = A * np.exp(a * t)
    _plot(t, x, title=f"Exponential: A={A}, a={a}")
    return t, x
