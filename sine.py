import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
frequency = 5  # Frequency in Hertz
amplitude = 1  # Amplitude of the sine wave
time_period = 1 / frequency  # Time period of the sine wave
sampling_rate = 1000  # Sampling rate in samples per second
time = np.linspace(0, 2 * time_period, int(sampling_rate))  # Time values


