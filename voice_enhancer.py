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
                      "Time(s)", "Amplitude", "'original' wave in the time domain","original_time_domain")

    # Plot the frequency domain
    fft_signal = fft(normal_wav)
    # fft_signal_magnitude = fft_signal/n_sample  # normalise the signal
    fft_signal_magnitude = fft_signal[0:int(n_sample/2)]
    freq_ratio = sampling_rate/n_sample
    frequency_axis = np.linspace(0, sampling_rate, int(n_sample/2))  # Frequency domain
    # frequency domain plot
    utils.plot_signal(frequency_axis, np.abs(fft_signal_magnitude), "linear",
                      "Frequency(Hz)", "Amplitude", "'original' wave in the frequency domain", "original_freq_domain")
    # amplitude (dB) vs frequency using logarithmic axis in the frequency domain
    frequency_axis = np.linspace(0, sampling_rate/2, int(n_sample / 2))  # Frequency domain
    amplitude_db = 20 * np.log10(fft_signal_magnitude)  # convert signal to amplitude
    utils.plot_signal(frequency_axis, amplitude_db, "log",
                      "Frequency(Hz)", "Amplitude", "'original' wave in the frequency domain", "original_freq_dB_domain")

    # Using Fourier transform to enhance the audio signal
    rate_a = 2
    #rate_b = 4
    lower_freq = int(6000/freq_ratio)
    upper_freq = int(12000/freq_ratio)
    fft_signal[lower_freq:upper_freq] = fft_signal[lower_freq:upper_freq] * rate_a
    fft_signal[n_sample-upper_freq+1:n_sample-lower_freq+1] = fft_signal[n_sample-upper_freq+1:n_sample-lower_freq+1]*rate_a
    # fft_signal[base - 1:base + 2] = 0
    # fft_signal[base-135:base+135] = fft_signal[base-135:base+135] * rate_b
    # fft_signal[n_sample-base-135:n_sample-base + 135] = fft_signal[n_sample-base-135:n_sample-base + 135] * rate_b
    # ifft, write to a new .wav 441 478 576
    enhanced_audio = ifft(fft_signal)
    enhanced_audio = utils.normalize_signal(enhanced_audio)
    utils.save_audio("improved.wav", sampling_rate, enhanced_audio)
    print("Audio enhanced successfully. Please check 'improved.wav' for result")






