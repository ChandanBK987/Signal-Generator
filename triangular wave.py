import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters for the triangular wave
frequency = 5  # Frequency in Hertz
amplitude = 1  # Amplitude of the triangular wave
time_period = 1 / frequency  # Time period of the wave
sampling_rate = 1000  # Sampling rate in samples per second
time = np.linspace(0, 2 * time_period, int(sampling_rate))  # Time values

# Generating the triangular wave
triangular_wave = amplitude * signal.sawtooth(2 * np.pi * frequency * time, 0.5)

