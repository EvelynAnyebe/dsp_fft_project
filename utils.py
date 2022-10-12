import scipy.io.wavfile as wavfile


def load_audio(filename):
    sampling_rate, wav = wavfile.read(filename)
    return sampling_rate, wav



