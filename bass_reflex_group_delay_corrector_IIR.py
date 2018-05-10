from scipy import signal
from scipy.io import wavfile
import math
import numpy as np
from pydub import AudioSegment

song = AudioSegment.from_mp3("/path/to/input/signal.mp3")
samples = song.get_array_of_samples()
samples = np.array(samples)
reversed_input_signal = samples[::-2]

# the filter parameters
fb = 40
fs = 44100
w = 2 * math.pi * fb / fs
r = 0.99

# IIR coefficients
b = [1, -2j / r * math.sin(w), - 1 / (r**2)]
a = [1,  2j * r * math.sin(w), - (r**2)]

# applying the filter on the reversed audio sequence
reversed_output_signal = signal.lfilter(b, a, reversed_input_signal)

reversed_output_signal = np.asarray(reversed_output_signal, dtype=np.int16)
output_signal = reversed_output_signal[::-1]
wavfile.write('out_signal.wav', fs, output_signal)
