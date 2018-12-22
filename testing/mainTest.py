import math
import wave, struct, myMath
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from fileIO.fileIO import read_whole, write_whole

# matplotlib.use("TkAgg")
from myMath.fourier import timeToFrequency, timeToFreq
from myMath.myWave import generateSineWave, addWaves

inputFilePath = "../input/guitar.wav"
outputFilePath = "../output/guitarNew.wav"
sampleRate = 48000.0 # hertz
duration = 5     # seconds
frequency = 20000  # hertz
frequency2 = 21000  # hertz
frequency3 = 22000  # hertz
noiseLen = 0.01
startOffset = 1

rt, params = read_whole(inputFilePath, duration)

cnt = 0
temp = []

amplitude = 0.1

noise = generateSineWave(params.framerate,noiseLen,amplitude,frequency)
noise2 = generateSineWave(params.framerate,noiseLen,amplitude,frequency2)
noise3 = generateSineWave(params.framerate,noiseLen,amplitude,frequency3)

# timeToFrequency(rt,params.framerate,duration)

frames = addWaves(rt, noise, startOffset * params.framerate)
frames = addWaves(frames, noise2,(startOffset + noiseLen)*params.framerate)
frames = addWaves(frames, noise3,(startOffset + 2*noiseLen)*params.framerate)

duration = 0.5

timeToFrequency([i[0] for i in frames[int(startOffset*params.framerate):int(startOffset*params.framerate+duration*params.framerate)]],params.framerate,duration)
# timeToFrequency([i[0] for i in frames],params.framerate,duration)
# timeToFrequency([i[0] for i in noise3],params.framerate,noiseLen)


# frames = addWaves(noise, noise2, 0, 1)
# timeToFreq([i[0] for i in frames],params.framerate,noiseLen)

write_whole(outputFilePath,params, frames)

