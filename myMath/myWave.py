import numpy as np

def generateSineWave(sRate, length, amplitude, freq):
    t = np.arange(0, length, 1/sRate)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return [[i] for i in wave]

def addWaves(target, source, startPosition):
    print("COMBINING WAVES...")
    startPosition = int(startPosition)
    frames = target[0:startPosition]
    cnt = 0
    for i in range(startPosition, len(target)):
        cnt += 1
        value = target[i]
        noiseFrame = [0,0] if cnt >= len(source) else source[cnt]
        # print("VALUE: " + str(value[0]) + ' ' + str(value[1]))
        # print("NOISE: " + str(noise))
        res = [0,0]
        if (noiseFrame[0] < 0):
            res[0] = max(-1, value[0] + noiseFrame[0])
            res[1] = max(-1, value[0] + noiseFrame[0])
        else:
            res[0] = min(1, value[0] + noiseFrame[0])
            res[1] = min(1, value[0] + noiseFrame[0])
        frames.append(res)
    return frames
