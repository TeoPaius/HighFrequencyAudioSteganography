import math
import wave, struct, myMath
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from fileIO.fileIO import read_whole, write_whole

# matplotlib.use("TkAgg")
from myMath.myWave import generateSineWave

inputFilePath = "../input/guitar.wav"
outputFilePath = "../output/guitarNew.wav"
sampleRate = 48000.0 # hertz
duration = 2       # seconds
frequency = 20000  # hertz

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

frames = []

amplitude = 0.5


noise = generateSineWave(params.framerate,10,0.5,frequency)


for i in rt:
    cnt+=1
    value = i
    noiseFrame = 0 if cnt >= len(noise) else noise[cnt]
    # print("VALUE: " + str(value[0]) + ' ' + str(value[1]))
    # print("NOISE: " + str(noise))
    res = [0,0]
    if(noiseFrame < 0):
        res[0] = max(-1, value[0] + noiseFrame)
        res[1] = max(-1, value[1] + noiseFrame)
    else:
        res[0] = min(1, value[0] + noiseFrame)
        res[1] = min(1, value[1] + noiseFrame)

    frames.append(res)

write_whole(outputFilePath,params, frames)

