import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from myMath import myWave



def timeToFrequency(samples, sRate, timeLen):
    Fs = sRate # sampling rate
    Ts = timeLen / Fs  # sampling interval

    t = np.arange(0, timeLen, Ts)  # time vector

    ff = 15000  # frequency of the signal

    n = len(y)  # length of the signal
    k = np.arange(n)
    T = n / Fs
    frq = k / T  # two sides frequency range
    frq = frq[range(int(n / 2))]  # one side frequency range

    Y = np.fft.fft(y) / n  # fft computing and normalization
    Y = Y[range(int(n / 2))]*2

    fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    ax = []
    ax.append(fig.add_subplot(2, 1, 1))
    ax.append(fig.add_subplot(2, 1, 2))
    fig.set_dpi(100)
    ax[0].plot(t, y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(frq, abs(Y), 'r')  # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')

    plt.show()

    return (frq, abs(Y))


y = myWave.generateSineWave(48000,3,0.5,10000)
timeToFrequency(y,48000,3)