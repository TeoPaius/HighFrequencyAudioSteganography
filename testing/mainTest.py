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
duration = 5       # seconds
frequency = 20000  # hertz
frequency2 = 21000  # hertz
frequency3 = 22000  # hertz
noiseLen = 0.01
startOffset = 1

# frequency2 = 500

# wavef = wave.open('sound.wav','w')
# wavef.setnchannels(1) # mono
# wavef.setsampwidth(2)
# wavef.setframerate(sampleRate)
#
# for i in range(int(duration * sampleRate)):
#     value = int(32767.0/2*myMath.cos(2*frequency*myMath.pi*float(i)/float(sampleRate)))
#     value2 = int(32767.0/2*myMath.cos(2*frequency2*myMath.pi*float(i)/float(sampleRate)))
#     data = struct.pack('<h', value + value2)
#     data2 = struct.pack('<h', value2)
#     wavef.writeframesraw(data)
#
#
# for i in range(int(duration * sampleRate)):
#     value = int(32767.0/2*myMath.cos(2*frequency*myMath.pi*float(i)/float(sampleRate)))
#
#     data = struct.pack('<h', value)
#
#     wavef.writeframesraw(data)
#
#
# for i in range(int(duration * sampleRate)):
#
#     value2 = int(32767.0/2*myMath.cos(2*frequency2*myMath.pi*float(i)/float(sampleRate)))
#
#     data2 = struct.pack('<h', value2)
#
#     wavef.writeframesraw(data2)
#
#
#
# wavef.writeframes(b'')
#
# wavef.close()

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

timeToFrequency([i[0] for i in frames],params.framerate,duration)
# timeToFrequency([i[0] for i in noise3],params.framerate,noiseLen)


# frames = addWaves(noise, noise2, 0, 1)
# timeToFreq([i[0] for i in frames],params.framerate,noiseLen)

write_whole(outputFilePath,params, frames)

