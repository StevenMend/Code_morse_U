import math
import struct
import sys


class MorseCode:
    def __init__(self, dit='.', dah='-'):
        self.dit = dit
        self.dah = dah
        self.morse_dict = {
            'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
            'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
            'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
            'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
            '9':'----.', '.':'.-.-.-', ',':'--..--', '?':'..--..', '!':'-.-.--',
            '/':'-..-.', '(':'-.--.', ')':'-.--.-', '&':'.-...', ':':'---...',
            ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-',
            '"':'.-..-.', "'":'.----.', '$':'...-..-', '@':'.--.-.'
        }

    def encode(self, text):
        return ' '.join(self.morse_dict.get(char.upper(), char) for char in text).replace('.', self.dit).replace('-',
                                                                                                                 self.dah)

    def decode(self, morse_code):
        reverse_morse = {v:k for k, v in self.morse_dict.items()}
        return ''.join(reverse_morse.get(code, code) for code in morse_code.split())

    def encode_exact(self, text):
        exact_timing = ' '.join(self.morse_dict.get(char.upper(), char) for char in text)
        return exact_timing.replace('.', self.dit).replace('-', self.dah)


class WaveGenerator:
    def __init__(self, sample_rate=8000, frequency=600, amplitude=0.8):
        self.sample_rate = sample_rate
        self.frequency = frequency
        self.amplitude = amplitude

    def generate_wave(self, duration):
        total_samples = int(self.sample_rate * duration)
        volume = self.amplitude * 32767
        return [int(math.sin(2 * math.pi * self.frequency * n / self.sample_rate) * volume) for n in
                range(total_samples)]


class WaveFileWriter:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.data = []

    def append_wave(self, wave_data):
        self.data.extend(wave_data)

    def save(self, filename):
        num_samples = len(self.data)
        with open(filename, 'wb') as f:
            # RIFF Header
            f.write(b'RIFF')
            f.write(struct.pack('<I', 36 + num_samples * 2))
            f.write(b'WAVE')
            # fmt Subchunk
            f.write(b'fmt ')
            f.write(struct.pack('<IHHIIHH', 16, 1, 1, self.sample_rate, self.sample_rate * 2, 2, 16))
            # data Subchunk
            f.write(b'data')
            f.write(struct.pack('<I', num_samples * 2))
            for sample in self.data:
                f.write(struct.pack('<h', sample))


def encode_text_to_morse_wave(text, filename):
    morse_code = MorseCode()  # Instanciar correctamente la clase
    encoded_text = morse_code.encode(text)
    encoded_exact_text = morse_code.encode_exact(text)
    print(f'"{text}" in Morse code:')
    print(encoded_text)

    sample_rate = 8000  # 8000 Hz
    frequency = 600  # 600 Hz
    dot_dur = 0.1  # 100 ms
    volume = 0.8  # 80%

    wave = WaveFileWriter(sample_rate)
    wave_duration = 0
    wave_data = []

    for c in encoded_exact_text:
        if c != ' ':
            wave_data += WaveGenerator(sample_rate, frequency, volume).generate_wave(
                dot_dur)  # Generar el punto o guion
            wave_duration += dot_dur
        else:
            wave_data += WaveGenerator(sample_rate, frequency, 0).generate_wave(dot_dur)  # Silencio para el espacio
            wave_duration += dot_dur

    wave.append_wave(wave_data)
    wave.save(filename)
    print(f"Audio saved as {filename}")  # Confirma que el archivo se guardó


def main():
    if len(sys.argv) == 3:
        encode_text_to_morse_wave(sys.argv[1], sys.argv[2])
    else:
        print('Usage: python script.py "text to convert" "filename.wav"')


if __name__ == '__main__':
    main()
