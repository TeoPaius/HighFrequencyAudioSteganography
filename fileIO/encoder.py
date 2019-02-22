from testing.config import *
import numpy as np


def messageToBits(message):
    result = []
    for c in message:
        bits = bin(ord(c))[2:]
        bits = "".join(['0' for i in range(0, int(np.log2(freqGranularity)))])[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def bitsToMessage(bitArray):
    chunksSize = int(np.log2(freqGranularity))
    chars = []
    for b in range(int(len(bitArray) / chunksSize)):
        byte = bitArray[b * chunksSize:(b + 1) * chunksSize]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def chunks(array, chuckSize):
    for i in range(0, len(array), chuckSize):
        yield array[i:i + chuckSize]

def bitsToFrequency(bitArray):
    chunksSize = int(np.log2(freqGranularity))
    assert(np.power(2,chunksSize) == freqGranularity )

    for chunk in chunks(bitArray, chunksSize):
        cnt = 0
        nr = 0
        for bit in chunk:
            nr = nr * 2 + bit
            cnt+=1
            if cnt % (chunksSize/subsampleFactor) == 0:
                frequency = startFreqCodingRange + freqInterval * 16 * nr
                print(str(chunk) + "----" + str(nr) + "-----" + str(frequency))
                nr = 0
                yield frequency



def frequencyToBits(frequencyArray):
    chunksSize = int(np.log2(freqGranularity))
    cnt = 0
    bits = []
    for frequency in frequencyArray:
        nr = int((frequency - startFreqCodingRange)/(freqInterval*16))
        buffer = []
        while nr != 0:
            buffer.append(nr%2)
            nr = int(nr/2)
        while len(buffer) % (chunksSize / 2) != 0:
            buffer.append(0)
        buffer.reverse()
        bits = bits + buffer
        cnt += 1
        if cnt % 2 == 0:
            yield bits


buffer = []
for i in bitsToFrequency(messageToBits("abacad")):
    buffer.append(i)
    if len(buffer) == 2:
        for j in frequencyToBits(buffer):
            print(j)
            print(bitsToMessage(j))
        buffer = []
    # print([j for j in frequencyToBits([i])])
    # print(bitsToMessage([j for j in frequencyToBits([i])]))