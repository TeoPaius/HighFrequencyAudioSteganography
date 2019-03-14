from fileIO.encoder import *
from myMath.fourier import timeToFrequency, detectFrequencyes
from myMath.myWave import generateSineWave, addWaves


def encodeMessage(message, frames,params, startFreqRange, endFreqRange):
    frequencies = [i for i in bitsToFrequency(messageToBits(message + "0"))]
    print(frequencies)
    currentOffset = 0
    for freq in frequencies:
        noise = generateSineWave(params.framerate,noiseLen,noiseAmplitude,freq)
        addWaves(frames, noise, (startOffset + currentOffset) * params.framerate)
        currentOffset += noiseLen
    return frames

def reconstructMessage(frames, params):
    currentOffset = 0
    moreData = True
    duration = scanWindow
    buffer = []
    result = []
    while moreData:
        frq, db, _ = timeToFrequency([i[0] for i in frames[int((startOffset + currentOffset) * params.framerate):int(
            (startOffset + currentOffset + duration) * params.framerate) + 1]], params.framerate, duration, startOffset)
        detectedFrequencies = detectFrequencyes(frq, db)
        print(detectedFrequencies)
        goodFreq = max(detectedFrequencies, key=lambda detection: detection[1])
        buffer.append(goodFreq[0])
        if(len(buffer) == 2):
            for j in frequencyToBits(buffer):
                result.append(bitsToMessage(j))
                print(result[-1])
                if result[-1] == "0":
                    moreData = False
            buffer = []
        currentOffset += duration

    return ''.join(result)[0:-1]