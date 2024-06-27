# %% Import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt

# %% Setup save directory
directory = "../plots"
if not os.path.exists(directory):
    os.makedirs(directory)

# %% Signal in Chunks
# Generate a sample signal
t = np.linspace(0, 10, 1000)
signal = np.sin(2 * np.pi * t) + 0.5 * np.random.randn(1000)

# Define chunk size
chunk_size = 100
chunks = [signal[i : i + chunk_size] for i in range(0, len(signal), chunk_size)]

# Plot the signal with chunks
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label="Original Signal", color="#2c0549")
for i, chunk in enumerate(chunks):
    plt.axvline(
        x=i * chunk_size / 100,
        color="red",
        linestyle="--",
        label="Chunk Boundary" if i == 0 else "",
    )
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal Divided into 1 Second Chunks")
plt.legend()
plt.savefig(os.path.join(directory, "signal_chunks.png"), dpi=300)
plt.show()

# %% Example of an FFT
# Generate a sample signal
t = np.linspace(0, 1, 1000)
signal = (
    np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t) + np.random.randn(len(t))
)

# Perform FFT
fft_values = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(signal), t[1] - t[0])

# Plot the FFT result
plt.figure(figsize=(12, 6))
plt.plot(fft_freq, np.abs(fft_values), color="#2c0549")
plt.xlim(0, 150)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT of the Signal")
plt.savefig(os.path.join(directory, "fft_example.png"), dpi=300)
plt.show()

# %% Typical Weekend Problem
# Generate a sample data retention scenario
days = np.arange(14)
data_retained = [
    1 if (i < 7 or i > 9) else 0 for i in days
]  # Retain data except for weekend days 7, 8, 9

# Plot the retention policy
plt.figure(figsize=(12, 6))
plt.bar(days, data_retained, color="#2c0549")
plt.xticks(days, [f"Day {i}" for i in days])
plt.xlabel("Days")
plt.ylabel("Data Retained (1 = Yes, 0 = No)")
plt.title("Typical Weekend Problem: Data Retention Policy")
plt.savefig(os.path.join(directory, "weekend_problem.png"), dpi=300)
plt.show()

# %%
