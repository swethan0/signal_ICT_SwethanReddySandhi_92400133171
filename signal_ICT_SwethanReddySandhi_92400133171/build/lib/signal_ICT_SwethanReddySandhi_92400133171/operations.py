import numpy as np

def time_shift(signal, k):
  
    signal = np.asarray(signal)
    return np.roll(signal, int(k))

def time_scale(signal, k):
    
    signal = np.asarray(signal, dtype=float)
    N = signal.size
    if k <= 0:
        raise ValueError("k must be positive")
    src_idx = np.linspace(0, N-1, N) / k
    src_idx = np.clip(src_idx, 0, N-1)
    i0 = np.floor(src_idx).astype(int)
    i1 = np.clip(i0 + 1, 0, N-1)
    frac = src_idx - i0
    return (1 - frac) * signal[i0] + frac * signal[i1]

def signal_addition(signal1, signal2):
    
    s1 = np.asarray(signal1, dtype=float)
    s2 = np.asarray(signal2, dtype=float)
    L = min(s1.size, s2.size)
    return s1[:L] + s2[:L]

def signal_multiplication(signal1, signal2):
    
    s1 = np.asarray(signal1, dtype=float)
    s2 = np.asarray(signal2, dtype=float)
    L = min(s1.size, s2.size)
    return s1[:L] * s2[:L]
