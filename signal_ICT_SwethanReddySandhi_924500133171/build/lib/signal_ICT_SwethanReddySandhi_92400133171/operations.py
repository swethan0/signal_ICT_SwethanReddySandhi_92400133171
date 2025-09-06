"""
operations.py
Functions:
- time_shift(signal, k)
- time_scale(signal, k)
- signal_addition(signal1, signal2)
- signal_multiplication(signal1, signal2)

Design note:
Each signal is expected as a tuple (t, x) where:
    t : numpy array of times/indices
    x : numpy array of samples
If a plain numpy array is provided, we assume t = np.arange(len(x)).

All functions return (t_out, x_out) and do not plot (plotting can be done in main).
"""

import numpy as np

def _unpack(signal):
    """Return (t, x) for input signal formats."""
    if isinstance(signal, tuple) and len(signal) == 2:
        return np.asarray(signal[0]), np.asarray(signal[1])
    else:
        x = np.asarray(signal)
        return np.arange(x.size), x

def time_shift(signal, k):
    """
    Shift in time by k units.
    If t is integer indices, shift adds k to indices (t -> t + k).
    For continuous-time t (float), k is added as seconds.
    Returns shifted (t_shifted, x)
    """
    t, x = _unpack(signal)
    t_shifted = t + k
    return t_shifted, x

def time_scale(signal, k):
    """
    Scale time axis by factor k.
    t_scaled = t * k
    Note: if k>1 -> stretches time (slower), if 0<k<1 -> compresses (faster).
    """
    t, x = _unpack(signal)
    t_scaled = t * k
    return t_scaled, x

def _align_and_operate(sig1, sig2, op):
    """Align two signals by union of t and perform op(x1, x2) where missing samples are 0."""
    t1, x1 = _unpack(sig1)
    t2, x2 = _unpack(sig2)
    # make both time vectors integer-index-friendly if they are integer-like
    # We'll use union of unique sorted times
    t_union = np.union1d(t1, t2)
    # prepare arrays filled with zero and then place values at matching times
    x1_full = np.zeros_like(t_union, dtype=float)
    x2_full = np.zeros_like(t_union, dtype=float)
    # map values
    # For float times, use exact matching; user should supply matching times where necessary
    for i, tt in enumerate(t_union):
        # find index in t1 where equal
        inds1 = np.where(t1 == tt)[0]
        inds2 = np.where(t2 == tt)[0]
        if inds1.size > 0:
            x1_full[i] = x1[inds1[0]]
        if inds2.size > 0:
            x2_full[i] = x2[inds2[0]]
    # operation
    if op == "add":
        return t_union, x1_full + x2_full
    elif op == "mul":
        return t_union, x1_full * x2_full
    else:
        raise ValueError("Unsupported operation")

def signal_addition(signal1, signal2):
    """Add two signals (aligned by time)"""
    return _align_and_operate(signal1, signal2, "add")

def signal_multiplication(signal1, signal2):
    """Point-wise multiply two signals (aligned by time)."""
    return _align_and_operate(signal1, signal2, "mul")
