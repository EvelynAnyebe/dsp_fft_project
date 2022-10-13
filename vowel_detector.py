# vowel detector module
from scipy.fft import fft
import utils
import numpy as np
from matplotlib import pyplot as plt


def vowel_detector(filename):
    sampling_rate, wav = utils.load_audio(filename)
    # Obtain and print parameters of the data
    n_sample = len(wav)
    time = n_sample / sampling_rate
    normal_wav = utils.normalize_signal(wav)

    print("The sampling rate is: " + str(sampling_rate))
    print("The number of samples is: " + str(n_sample))
    print("The Total recording time is: " + str(int(time)))
    print("Max sample: " + str(np.max(np.abs(wav))))
    print("Min sample: " + str(np.min(np.abs(wav))))

    # vowels and consonants
    time_axis = np.arange(0, time, (1 / sampling_rate))  # Time domain
    fft_signal = fft(normal_wav)
    # fft_signal_magnitude = fft_signal/n_sample  # normalise the signal
    fft_signal_magnitude = fft_signal[0:int(n_sample / 2)]
    freq_ratio = sampling_rate / n_sample
    frequency_axis = np.linspace(0, sampling_rate, int(n_sample / 2))  # Frequency domain
    # frequency domain plot
    # amplitude (dB) vs frequency using logarithmic axis in the frequency domain
    frequency_axis = np.linspace(0, sampling_rate / 2, int(n_sample / 2))  # Frequency domain
    amplitude_db = 20 * np.log10(fft_signal_magnitude)  # convert signal to amplitude
    base = np.argmax(np.abs(fft_signal_magnitude))
    base_f = round(base*freq_ratio, 2)
    plt.plot(frequency_axis, amplitude_db, "blue")
    plt.xscale("log")
    vowel_peak = [441, 478, 576]



