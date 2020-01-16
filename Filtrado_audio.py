# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:48:57 2020

@author: Michae
"""

import wave
import numpy
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import filtfilt
from scipy.fftpack import fft,ifft

#abrir el archivoy encontrar todas las caracteristicas del audio 
spf = wave.open('ragnar.wav','rb')
(nChannels, sampWidth, sampleRate, nFrames, compType, compName) = spf.getparams()
#sampleRate la fecuencia de muestreo 
nFrames

# extract audio from wav file
input_signal = spf.readframes(-1)
input_signal = numpy.fromstring(input_signal, 'Int16')
spf.close()

plt.plot(input_signal)
plt.show()

#revisar las comonentes en frecuencia 
freq_domain_signal = fft(input_signal)
plt.plot(freq_domain_signal)
plt.xlim(0,300000)
plt.show()


# create the filter
#voz=250Hz-3KHz 
#samplerate=44000 -> señal=22000 (ajustar la señal a mejor manera)
N = 4
nyq =  sampleRate*0.5
low =200#Hz
high = 100#Hz

#Diseño filtro pasa altos
#componentes en frecuencia (b,a)
b, a = signal.butter(N,1000,fs=3000,analog=False, btype='lp') #hp o high pasa altos 
#sos= componentes en series de tiempo
sos=signal.butter(N, 1000,fs=3000, btype='hp',analog=False, output='sos') #hp o high pasa altos
plt.plot(sos)
plt.show() 

# apply filter
output_signal = signal.filtfilt(b, a, input_signal)

# ceate output file
#r=read,w=write
wav_out = wave.open("output5.wav", "w")
#int(4*sampleRate)=reducir el numero de componentes que duplican el tiempo
wav_out.setparams((nChannels, sampWidth, int(4*sampleRate), nFrames, compType, compName))

# write to output file
wav_out.writeframes(output_signal.tobytes())
wav_out.close()

# plot the signals
plt.plot( input_signal, label='Input')
plt.plot(output_signal, label='Output')
plt.show()

