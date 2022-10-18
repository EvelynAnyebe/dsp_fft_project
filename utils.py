import scipy.io.wavfile as wavfile
import numpy as np
from matplotlib import pyplot as plt


def load_audio(filename):
    sampling_rate, wav = wavfile.read(filename)
    return sampling_rate, wav


def save_audio(filename, sample_rate, wav):
    wavfile.write(filename, sample_rate, wav)


def normalize_signal(audio_signal):
    sig = np.int16((audio_signal/np.max(np.abs(audio_signal))*2**15))
    #sig = audio_signal/2**15
    return sig


def plot_signal(x, y, scale, x_label, y_label, title, out_image):
    plt.figure()
    plt.plot(x, y, 'blue')
    if scale == "log":
        plt.xscale("log")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.savefig(out_image, format="svg")
    plt.show()
