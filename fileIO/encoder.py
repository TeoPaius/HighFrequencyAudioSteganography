from testing.config import *
import numpy as np


def messageToBits(message):
    result = []
    for c in message:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def bitsToMessage(bitArray):
    chars = []
    for b in range(int(len(bitArray) / 8)):
        byte = bitArray[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def chunks(array, chuckSize):
    for i in range(0, len(array), chuckSize):
        yield array[i:i + chuckSize]

def bitsToFrequency(bitArray):
    chunksSize = int(np.log2(freqGranularity))
    assert(np.power(2,chunksSize) == freqGranularity )

    for chunk in chunks(bitArray, chunksSize):
        nr = 0
        for bit in chunk:
            nr = nr * 2 + bit
        frequency = startFreqCodingRange + freqInterval * nr
        print(str(chunk) + "----" + str(nr) + "-----" + str(frequency))
        yield frequency


for i in bitsToFrequency(messageToBits("abaaaa")):
    pass