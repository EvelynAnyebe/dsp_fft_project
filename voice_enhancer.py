# module for voice enhancement

import utils
import numpy as  np
import numpy as np
from matplotlib import pyplot as plt


def fft_enhancer(filename):
    sampling_rate, wav = utils.load_audio(filename)
    # Obtain and print parameters of the data
    rec_time = len(wav) / sampling_rate
    print("The sampling rate is: " + str(sampling_rate))
    print("The number of samples is: " + str(len(wav)))
    print("The Total recording time is: " + str(int(rec_time)))

    # plotting audio signal
    # Create vectors for the x-axis of the time and frequency domain plots
    taxis = np.linspace(0, rec_time, len(wav))  # Time domain
    faxis = np.linspace(0, sampling_rate, len(wav))  # Frequency domain

    # time domain plot
    'Plot the audio signal in the time domain'
    plt.subplot(211)  # Top of two vertically stacked graphs with one column
    plt.plot(taxis, wav, 'blue')
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.title('Time domain plot of original audio signal')
    plt.show()


