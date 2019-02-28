import math
import wave, struct, myMath
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from controller.logic import encodeMessage, reconstructMessage
from myMath.fourier import detectFrequencyes
from fileIO.fileIO import read_whole, write_whole

# matplotlib.use("TkAgg")
from myMath.fourier import timeToFrequency, timeToFreq
from myMath.myWave import generateSineWave, addWaves
from testing.config import *

inputFilePath = "../input/guitar.wav"
outputFilePath = "../output/guitarNew.wav"
duration = defaultStegoFileDuration     # seconds
frequency = 21240  # hertz
frequency2 = 22440  # hertz
frequency3 = 21480 # hertz



rt, params = read_whole(inputFilePath, duration)

cnt = 0
temp = []



# noise = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency)
# noise2 = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency2)
# noise3 = generateSineWave(params.framerate,noiseLen,noiseAmplitude,frequency3)

# timeToFrequency(rt,params.framerate,duration)
# addWaves(rt, noise, startOffset * params.framerate)
# addWaves(rt, noise2,(startOffset + noiseLen)*params.framerate)
# addWaves(rt, noise3,(startOffset + 2*noiseLen)*params.framerate)

message = "versurile bibliei in abi- papuci ggucci"
frames = encodeMessage(message, rt, params, 0, 0)
result = reconstructMessage(frames,params)
print("initial message: "+message)
print("decode message: " + result[0:-1])

# startOffset = 1.0
# duration = 0.01
# frq, db, _ = timeToFrequency([i[0] for i in frames[int(startOffset*params.framerate):int((startOffset+ duration)*params.framerate)+1]],params.framerate,duration,startOffset)
#
# detectedFrequencies = detectFrequencyes(frq, db)
# print("detected: " + str(detectedFrequencies))
# timeToFrequency([i[0] for i in frames],params.framerate,duration)
# timeToFrequency([i[0] for i in noise3],params.framerate,noiseLen)


# frames = addWaves(noise, noise2, 0, 1)
# timeToFreq([i[0] for i in frames],params.framerate,noiseLen)

write_whole(outputFilePath,params, frames)
# rt2, params2 = read_whole(outputFilePath, defaultStegoFileDuration)
# frames2 = rt2
# duration2 = scanWindow
# startOffset2 = 1.0
# duration2 = 0.05
# frq2, db2 = timeToFrequency([i[0] for i in frames[int(startOffset2*params.framerate):int((startOffset2+ duration2)*params.framerate)+1]],params.framerate,duration2,startOffset2)
#
# detectFrequencyes(frq2, db2)
