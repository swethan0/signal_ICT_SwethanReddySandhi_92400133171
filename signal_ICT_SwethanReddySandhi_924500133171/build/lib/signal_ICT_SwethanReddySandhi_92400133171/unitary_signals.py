"""
unitary_signals.py
Functions:
- unit_step(n)
- unit_impulse(n)
- ramp_signal(n)

Each function returns a tuple (t, x) where t is integer index vector and x is numpy array,
and also plots the signal using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

def _plot(t, x, title="Signal", xlabel="n", ylabel="Amplitude", stem=True):
    plt.figure(figsize=(8,3))
    if stem:
        markerline, stemlines, baseline = plt.stem(t, x)
        plt.setp(markerline, markersize=6)
    else:
        plt.plot(t, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def unit_step(n):
    """
    Generate unit step u[n] for n length or for indices given in list/array.
    Usage:
        t, x = unit_step(20)            # n=0..19
        t, x = unit_step(np.arange(-5,15))  # custom indices
    Returns: (t, x)
    """
    if isinstance(n, (list, tuple, np.ndarray)):
        t = np.asarray(n)
    else:
        t = np.arange(n)
    x = (t >= 0).astype(float)
    _plot(t, x, title="Unit Step Signal u[n]")
    return t, x

def unit_impulse(n):
    """
    Generate unit impulse delta[n] for length or indices.
    By default impulse at n==0.
    """
    if isinstance(n, (list, tuple, np.ndarray)):
        t = np.asarray(n)
    else:
        t = np.arange(n)
    x = (t == 0).astype(float)
    _plot(t, x, title="Unit Impulse Signal δ[n]")
    return t, x

def ramp_signal(n):
    """
    Generate ramp signal r[n] = n for n>=0 else 0.
    """
    if isinstance(n, (list, tuple, np.ndarray)):
        t = np.asarray(n)
    else:
        t = np.arange(n)
    x = np.where(t >= 0, t.astype(float), 0.0)
    _plot(t, x, title="Ramp Signal r[n]")
    return t, x
