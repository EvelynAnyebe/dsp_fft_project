# module for voice enhancement
from scipy.fft import fft, ifft
import utils
import numpy as np
from matplotlib import pyplot as plt


def fft_enhancer(filename):
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

    # plot the time domain - Normalised Amplitude vs Time
    # Create vectors for the x-axis of the time
    time_axis = np.arange(0, time, (1/sampling_rate))  # Time domain
    utils.plot_signal(time_axis,  normal_wav, "linear",
                      "Time(s)", "Amplitude", "'original' wave in the time domain","original_time_domain.svg")

    # Plot the frequency domain
    fft_signal = np.fft.fft(normal_wav)
    fft_signal_magnitude = np.abs((fft_signal[0:int(n_sample/2)]/n_sample))  # remove imaginary part
    freq_ratio = sampling_rate/n_sample
    frequency_axis = np.linspace(0, sampling_rate/2, int(n_sample/2))  # Frequency domain
    # frequency domain plot
    utils.plot_signal(frequency_axis, fft_signal_magnitude, "linear",
                      "Frequency(Hz)", "Amplitude", "'original' wave in the frequency domain", "original_freq_domain.svg")
    # amplitude (dB) vs frequency using logarithmic axis in the frequency domain
    amplitude_db = 20 * np.log10(fft_signal_magnitude)  # convert signal to amplitude
    utils.plot_signal(frequency_axis, amplitude_db, "log",
                      "Frequency(Hz)", "Amplitude", "'original' wave in the frequency domain", "original_freq_dB_domain.svg")

    # Using Fourier transform to enhance the audio signal
    base_index = np.argmax(fft_signal_magnitude)
    base_freq = round(base_index*freq_ratio, 2)
    print("f0: ", base_freq)

    lower_freq = int(150/freq_ratio)
    upper_freq = int(1025/freq_ratio)
    fft_signal[lower_freq:upper_freq] = fft_signal[lower_freq:upper_freq] * 4
    fft_signal[n_sample-upper_freq+1:n_sample-lower_freq+1] = fft_signal[n_sample-upper_freq+1:n_sample-lower_freq+1]\
        * 4
    fft_signal_magnitude = np.abs((fft_signal[0:int(n_sample/2)]/n_sample))  # remove imaginary part
    amplitude_db = 20 * np.log10(fft_signal_magnitude)  # convert signal to amplitude
    utils.plot_signal(frequency_axis, amplitude_db, "log",
                      "Frequency(Hz)", "Amplitude", "'Improved' wave in the frequency domain", "improved_freq_dB_domain.svg")
    enhanced_audio = ifft(fft_signal)
    enhanced_audio = utils.normalize_signal(enhanced_audio)
    utils.save_audio("improved.wav", sampling_rate, enhanced_audio)
    print("Audio enhanced successfully. Please check 'improved.wav' for result")
