import math
import wave, struct, myMath
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from myMath.fourier import detectFrequencyes
from fileIO.fileIO import read_whole, write_whole

# matplotlib.use("TkAgg")
from myMath.fourier import timeToFrequency, timeToFreq
from myMath.myWave import generateSineWave, addWaves
from testing.config import *

inputFilePath = "../input/guitar.wav"
outputFilePath = "../output/guitarNew.wav"
duration = defaultStegoFileDuration     # seconds
frequency = 24000  # hertz
frequency2 = 24250  # hertz
frequency3 = 24500 # hertz



rt, params = read_whole(inputFilePath, duration)

cnt = 0
temp = []



noise = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency)
noise2 = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency2)
noise3 = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency3)

# timeToFrequency(rt,params.framerate,duration)

frames = addWaves(rt, noise, startOffset * params.framerate)
frames = addWaves(rt, noise2,(startOffset + noiseLen)*params.framerate)
frames = addWaves(rt, noise3,(startOffset + 2*noiseLen)*params.framerate)
frames = rt
duration = scanWindow
startOffset = 1.0
duration = 0.1
frq, db = timeToFrequency([i[0] for i in frames[int(startOffset*params.framerate):int((startOffset+ duration)*params.framerate)+1]],params.framerate,duration,startOffset)

detectFrequencyes(frq, db)
# timeToFrequency([i[0] for i in frames],params.framerate,duration)
# timeToFrequency([i[0] for i in noise3],params.framerate,noiseLen)


# frames = addWaves(noise, noise2, 0, 1)
# timeToFreq([i[0] for i in frames],params.framerate,noiseLen)

write_whole(outputFilePath,params, frames)

