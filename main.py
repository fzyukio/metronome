import argparse

import numpy as np

from wavfile import write

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file-name', dest='filename', action='store', type=str, required=True,
                    help='Gap length between two pulse in milliseconds')
parser.add_argument('--gap-length', dest='gap_ms', action='store', type=int, required=True,
                    help='Gap length between two pulse in milliseconds')
parser.add_argument('--duration', dest='duration_ms', action='store', type=int, required=True,
                    help='Duration of the file in milliseconds')
parser.add_argument('--fs', dest='fs', action='store', type=int, default=48000, help='Sample rate')

args = parser.parse_args()

gap_ms = args.gap_ms
duration_ms = args.duration_ms
fs = args.fs
bits = 16
filename = args.filename

bytes = bits // 8
dtype = '<i%d' % bytes

nsamples = duration_ms * fs // 1000
gap_length = gap_ms * fs // 1000

beep_length = 10 * fs // 1000
half_beep_length = beep_length // 2

array = np.zeros((nsamples,), dtype=np.float32)

frequency = 440
length = 5

beep_t = np.linspace(0, 1, beep_length)  # Produces a 5 second Audio-File
beep_value_array = np.sin(frequency * 2 * np.pi * beep_t)  # Has frequency of 440Hz

previous_beep_position = 0
array[:half_beep_length] = beep_value_array[half_beep_length:]
while True:
    current_beep_position = previous_beep_position + gap_length

    if current_beep_position + half_beep_length > nsamples:
        if current_beep_position - half_beep_length < nsamples:
            last_beep_length = nsamples - (current_beep_position - half_beep_length)
            array[current_beep_position - half_beep_length:] = beep_value_array[:last_beep_length]
        break

    array[current_beep_position - half_beep_length:current_beep_position + half_beep_length] = beep_value_array
    previous_beep_position = current_beep_position

array[array > 1.0] = 1.0
array[array < -1.0] = -1.0
data = np.asarray(array * (2 ** 31 - 1), dtype=np.int32).astype(dtype)

uint8_data = np.frombuffer(data.tobytes(), dtype=np.uint8).reshape((nsamples, 1, bytes))

write(filename, fs, uint8_data, bitrate=bits)
