import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from myMath import myWave
from scipy.fftpack import fft as fftScy

refAmplitude = 0.00001

def timeToFrequency(samples, sRate, timeLen):
    Fs = sRate # sampling rate
    Ts = 1 / Fs  # sampling interval

    t = np.arange(0, timeLen, Ts)  # time vector


    n = timeLen*sRate  # length of the signal
    k = np.arange(n)
    T = n / Fs
    frq = k / T  # two sides frequency range
    frq = frq[range(int(n / 2))]  # one side frequency range

    Y = np.fft.fft(samples) / n  # fft computing and normalization
    Y = abs(Y[range(int(n / 2))]*2)

    fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    ax = []
    ax.append(fig.add_subplot(2, 1, 1))
    ax.append(fig.add_subplot(2, 1, 2))
    fig.set_dpi(100)
    ax[0].plot(t, samples[:int(timeLen*sRate)])
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(frq, [max(i, 0) for i in 20*np.log10(Y/refAmplitude)], 'r')  # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('dB')

    plt.show()

    return (frq, abs(Y))


def timeToFreq(samples, sRate, timeLen):
    N = len(samples)

    T = 1.0 / sRate
    x = np.linspace(0.0, N * T, N)
    y = samples
    yf = np.fft.fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
    plt.grid()
    plt.show()

#
# y = myWave.generateSineWave(48000,3,0.5,10000)
# timeToFrequency(y,48000,3)