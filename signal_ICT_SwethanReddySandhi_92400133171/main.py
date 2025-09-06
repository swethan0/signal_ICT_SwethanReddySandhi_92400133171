import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_SwethanReddySandhi_92400133171 import unitary_signals, trigonometric_signals, operations

# 1) Unit step and unit impulse (length 20: n=-10..9)
n = np.arange(-10, 10)
step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)

# 2) Sine wave: A=2, f=5 Hz, phi=0, t in [0,1) with 1000 samples
t = np.linspace(0, 1, 1000, endpoint=False)
sine = trigonometric_signals.sine_wave(2, 5, 0, t)

# 3) Time shift sine by +5 samples and plot both
shifted = operations.time_shift(sine, +5)
plt.plot(t, sine, label="Original sine")
plt.plot(t, shifted, label="Shifted by +5 samples")
plt.title("Time Shift: sine vs shifted")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# 4) Addition: unit step + ramp
ramp = unitary_signals.ramp_signal(n)
added = operations.signal_addition(step, ramp)
plt.stem(n[:len(added)], added)
plt.title("Addition: step + ramp")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# 5) Multiply sine and cosine of same frequency
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
product = operations.signal_multiplication(sine, cosine)
plt.plot(t[:len(product)], product)
plt.title("Multiplication: sine × cosine (same f)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
