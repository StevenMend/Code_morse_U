# Morse Code Audio Generator

This Python project converts text into Morse code and generates a WAV audio file that reproduces the corresponding Morse code sounds.

## Description

The program takes a string of text as input and converts it into Morse code. It generates an audio file that simulates the sounds of dots and dashes, where:
- **Dots** are represented as short tones.
- **Dashes** are represented as longer tones.
- **Spaces** between letters and words are represented as silence.

The conversion process is handled by the **MorseCode** class, which provides methods for encoding and decoding text. The **WaveGenerator** class is used to create sound waves for the Morse code representation, while the **WaveFileWriter** class writes the generated audio data into a WAV file format.

The main function, `encode_text_to_morse_wave`, manages the entire process of converting text to Morse code, generating the audio waves, and saving the result to a file. The script can be executed from the command line, making it user-friendly and efficient.

## Requirements

- Python 3.x
- Required modules: `math`, `struct`, `sys`

## Usage

To run the script, use the following command in the terminal:

```bash
python script.py "text to convert" "output_filename.wav"
# Code_morse_U
