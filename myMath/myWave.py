import numpy as np

def generateSineWave(sRate, length, amplitude, freq):
    t = np.arange(0,length, length/sRate)
    wave = amplitude * np.sin(2 * np.pi * freq/length * t)
    return wave
