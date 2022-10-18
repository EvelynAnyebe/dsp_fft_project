# This is a python script runs voice_enhancer.py and vowel_detector.py
import sys
import voice_enhancer as vh
import vowel_detector as vd

# Hitec10T@202#IPsZon


def fft_processor():
    try:
        original_audio_file = "original.wav"
        vowel1 = "vowel1.wav"
        vowel2 = "vowel2.wav"
        vh.fft_enhancer(original_audio_file)
        # vd.vowel_detector(original_audio_file)

        print("\n\nProgram completed successfully.")
    except TypeError as e:
        print(e)
        sys.exit(1)
    except IndexError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except NameError as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nProgram interrupted.")
        sys.exit(1)


if __name__ == '__main__':
    fft_processor()

