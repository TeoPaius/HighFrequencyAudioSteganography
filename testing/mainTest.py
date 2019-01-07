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
from testing.config import *

inputFilePath = "../input/guitar.wav"
outputFilePath = "../output/guitarNew.wav"
duration = defaultStegoFileDuration     # seconds
frequency = 20000  # hertz
frequency2 = 20200  # hertz
frequency3 = 20500  # hertz



rt, params = read_whole(inputFilePath, duration)

cnt = 0
temp = []



noise = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency)
noise2 = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency2)
noise3 = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency3)

# timeToFrequency(rt,params.framerate,duration)

frames = addWaves(rt, noise, startOffset * params.framerate)
frames = addWaves(frames, noise2,(startOffset + noiseLen)*params.framerate)
frames = addWaves(frames, noise3,(startOffset + 2*noiseLen)*params.framerate)

duration = scanWindow
startOffset = 0.95
duration = 0.15
timeToFrequency([i[0] for i in frames[int(startOffset*params.framerate):int(startOffset*params.framerate+duration*params.framerate)]],params.framerate,duration,startOffset)
# timeToFrequency([i[0] for i in frames],params.framerate,duration)
# timeToFrequency([i[0] for i in noise3],params.framerate,noiseLen)


# frames = addWaves(noise, noise2, 0, 1)
# timeToFreq([i[0] for i in frames],params.framerate,noiseLen)

write_whole(outputFilePath,params, frames)

