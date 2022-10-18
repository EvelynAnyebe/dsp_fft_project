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
