import numpy as np

def generateSineWave(sRate, length, amplitude, freq):
    t = np.arange(0, length, 1/sRate)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave
