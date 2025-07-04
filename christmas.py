import numpy as np
from scipy.io.wavfile import write
import pygame
import time
import os

# 1. Generate WAV files if not exist
def generate_sine_wave(filename, freq, duration=0.5, sample_rate=44100):
    if os.path.exists(filename):
        return  # Don’t overwrite
    print(f"Generating {filename}...")
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi)
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    write(filename, sample_rate, audio)

notes_freqs = {
    "C4.wav": 261.63,
    "D4.wav": 293.66,
    "E4.wav": 329.63,
    "F4.wav": 349.23,
    "G4.wav": 392.00,
    "A4.wav": 440.00,
    "B4.wav": 493.88,
}

for file, freq in notes_freqs.items():
    generate_sine_wave(file, freq)

# 2. Initialize pygame mixer
pygame.mixer.init()
pygame.init()

# 3. Map MIDI notes to filenames
notes_files = {
    60: "C4.wav",
    62: "D4.wav",
    64: "E4.wav",
    65: "F4.wav",
    67: "G4.wav",
    69: "A4.wav",
    71: "B4.wav",
}

# 4. Jingle Bells notes and durations
notes = [
    64, 64, 64, 64, 64, 64,  # E E E E E E
    64, 67, 60, 62, 64,      # E G C D E
    65, 65, 65, 65, 65, 64, 64, 64, 64, 62, 62, 64, 62, 67  # F F F F F E E E E D D E D G
]

durations = [
    0.4, 0.4, 0.8, 0.4, 0.4, 0.8,
    0.4, 0.4, 0.4, 0.4, 1.0,
    0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 1.2
]

# 5. Play the tune
print("""
         |
        -+-
         A
        /=\               /\  /\    ___  _ __  _ __ __    __
      i/ O \i            /  \/  \  / _ \| '__|| '__|\ \  / /
      /=====\           / /\  /\ \|  __/| |   | |    \ \/ /
      /  i  \           \ \ \/ / / \___/|_|   |_|     \  /
    i/ O * O \i                                       / /
    /=========\        __  __                        /_/    _
    /  *   *  \        \ \/ /        /\  /\    __ _  ____  | |
  i/ O   i   O \i       \  /   __   /  \/  \  / _` |/ ___\ |_|
  /=============\       /  \  |__| / /\  /\ \| (_| |\___ \  _
  /  O   i   O  \      /_/\_\      \ \ \/ / / \__,_|\____/ |_|
i/ *   O   O   * \i
/=================\
       |___|                                                   
""")

for note, dur in zip(notes, durations):
    filename = notes_files.get(note)
    if filename:
        sound = pygame.mixer.Sound(filename)
        sound.play()
        time.sleep(dur)
    else:
        time.sleep(dur)  # rest or unsupported note

print("Process Completed.")