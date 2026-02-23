import numpy as np
import matplotlib.pyplot as plt

def simulate_digitization(analog_signal, sampling_rate, quantization_levels):

    t_continuous = np.linspace(0, 1, 1000)
    x_continuous = analog_signal(t_continuous)

    # Sampling
    t_sampled = np.linspace(0, 1, sampling_rate)
    x_sampled = analog_signal(t_sampled)

    # Quantization
    x_min = np.min(x_sampled)
    x_max = np.max(x_sampled)

    delta = (x_max - x_min) / (quantization_levels - 1)
    x_quantized = np.round((x_sampled - x_min) / delta) * delta + x_min

    plt.figure(figsize=(12,8))

    # Analog
    plt.subplot(3,1,1)
    plt.plot(t_continuous, x_continuous)
    plt.title("Sinyal Analog Kontinu")

    # Sampling
    plt.subplot(3,1,2)
    plt.plot(t_continuous, x_continuous)
    plt.stem(t_sampled, x_sampled)
    plt.title("Hasil Sampling")

    # Quantization
    plt.subplot(3,1,3)
    plt.plot(t_continuous, x_continuous)
    plt.step(t_sampled, x_quantized, where="mid")
    plt.scatter(t_sampled, x_quantized)
    plt.title("Hasil Quantization")

    plt.tight_layout()
    plt.show()

    print("="*50)
    print("Sampling rate       :", sampling_rate)
    print("Quantization levels :", quantization_levels)
    print("Resolusi kuantisasi :", delta)

    return t_sampled, x_sampled, x_quantized


# Contoh sinyal
def analog_signal(t):
    return np.sin(2 * np.pi * 5 * t)

simulate_digitization(
    analog_signal=analog_signal,
    sampling_rate=20,
    quantization_levels=8
)
