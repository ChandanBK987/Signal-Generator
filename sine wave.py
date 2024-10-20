import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
frequency = 5  # Frequency in Hertz
amplitude = 1  # Amplitude of the sine wave
time_period = 1 / frequency  # Time period of the sine wave
sampling_rate = 1000  # Sampling rate in samples per second
time = np.linspace(0, 2 * time_period, int(sampling_rate))  # Time values

# Generating the sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

# Plotting the sine wave
plt.plot(time, sine_wave)
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
