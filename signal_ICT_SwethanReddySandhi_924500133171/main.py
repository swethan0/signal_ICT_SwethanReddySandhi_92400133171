"""
main.py
Demonstrates:
- Generate and plot unit step & unit impulse (length 20)
- Generate sine wave: A=2, f=5Hz, phi=0, t=0..1s
- Time shift sine by +5 units (here 'units' will be seconds) and plot both
- Add unit step and ramp signal and plot result
- Multiply a sine and cosine (same freq) and plot result
"""

import numpy as np
import matplotlib.pyplot as plt

from signal_ICT_SwethanReddySandhi_92400133171 import (
    unit_step, unit_impulse, ramp_signal,
    sine_wave, cosine_wave,
    time_shift, time_scale, signal_addition, signal_multiplication
)

def plot_pair(t1, x1, t2=None, x2=None, title="Signals", labels=("sig1", "sig2")):
    plt.figure(figsize=(9,3))
    plt.plot(t1, x1, label=labels[0])
    if t2 is not None and x2 is not None:
        plt.plot(t2, x2, label=labels[1], linestyle='--')
    plt.title(title)
    plt.xlabel("t / n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # 1) Unit step & impulse (length 20)
    t_step, x_step = unit_step(20)     # t 0..19
    t_imp, x_imp = unit_impulse(20)
    # (both are already plotted inside functions)
    # Combine and plot together for clarity:
    plot_pair(t_step, x_step, t_imp, x_imp, title="Unit Step and Unit Impulse", labels=("u[n]", "δ[n]"))

    # 2) Sine wave: A=2, f=5Hz, phi=0, t=0..1s
    fs = 1000  # sampling freq for smooth plot
    t = np.linspace(0, 1, int(fs*1)+1)
    t_sine, x_sine = sine_wave(2, 5, 0, t)  # plotted inside
    # 3) Time shift the sine by +5 units (seconds). We'll shift time axis by +5
    t_shifted, x_shifted = time_shift((t_sine, x_sine), 5)
    plot_pair(t_sine, x_sine, t_shifted, x_shifted, title="Original and Time-shifted Sine (shift +5s)", labels=("original", "shifted"))

    # 4) Addition of unit step and ramp signal (use same indices)
    # create indices -5..14 to show negative indices as well
    indices = np.arange(-5, 15)
    t_u, x_u = unit_step(indices)
    t_r, x_r = ramp_signal(indices)
    t_add, x_add = signal_addition((t_u, x_u), (t_r, x_r))
    # Plot
    plt.figure(figsize=(8,3))
    plt.stem(t_add, x_add)
    plt.title("Addition of Unit Step and Ramp")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 5) Multiply sine and cosine of same frequency
    # generate both on t=0..1s
    t0 = np.linspace(0,1,1001)
    _, s = sine_wave(1.0, 5, 0, t0)   # plotted inside
    _, c = cosine_wave(1.0, 5, 0, t0) # plotted inside
    t_mul, x_mul = signal_multiplication((t0, s), (t0, c))
    plt.figure(figsize=(9,3))
    plt.plot(t_mul, x_mul)
    plt.title("Point-wise Multiplication: sine * cosine")
    plt.xlabel("t (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
