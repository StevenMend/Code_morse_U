from pydub import AudioSegment
from pydub.playback import play

def play_wav_file(filename):
    # Cargar el archivo WAV
    audio = AudioSegment.from_file(filename)
    # Reproducir el audio
    play(audio)

if __name__ == '__main__':
    # Nombre del archivo WAV que deseas reproducir
    wav_file_name = "morseaudio.wav"  # Reemplaza con el nombre de tu archivo
    play_wav_file(wav_file_name)
