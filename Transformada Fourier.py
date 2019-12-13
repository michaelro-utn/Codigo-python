# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:33:06 2019

@author: Michae
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab as pl
from IPython import display
import time as ttime
import random
from mpl_toolkits.mplot3d import Axes3D #generar graficos en 3D
from scipy.stats import pearsonr as pr

#generar puntos complejos 
z1=complex(2,3)
print ("Número complejo N1: ",z1)
z2=complex(5,-5)
print ("Número complejo N2: ",z2)
z3=complex(4,2)
print ("Número complejo N3: ",z3)

#generar señales 
amp=2
phase= np.pi
freq=25
freq2=75/2
srate = 500; # sampling rate in Hz
time  = np.arange(0.,0.25,1./srate) # time in seconds
sinewave1=amp*np.cos(2*np.pi*freq*time)
sinewave2=amp*np.cos(2*np.pi*freq2*time+phase)

#sumar puntos complejos 
print("Suma de números complejos")
zt1=z1+z2
print("Resultado entre N1+N2", zt1)
plt.plot(np.real(zt1),np.imag(zt1),'mo',label='zt1') #'bo' circunferencia de color azul
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.legend(loc='best')
plt.grid()
plt.show()
#multiplicación de complejos 
print("Mulipicación de numeros complejos")
zt2=z2*z3
print("Resultado entre N2*N3", zt2)
plt.plot(np.real(zt2),np.imag(zt2),'bo',label='zt2') #'bo' circunferencia de color azul
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.legend(loc='best')
plt.grid()
plt.show()
#division de complejos 
print("División de números complejos")
zt3=z3/z2
print("Resultado entre N3/N2", zt3)
plt.plot(np.real(zt3),np.imag(zt3),'co',label='zt2') #'bo' circunferencia de color azul
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.legend(loc='best')
plt.grid()
plt.show()
#exponencial de la función 1 
print ("Exponencial 1era señal")
zt4=np.exp(sinewave1)

fig=plt.figure()
plt.plot(time,zt4)
plt.grid()
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(time,np.real(zt4),np.imag(zt4))
ax.set_xlabel('Time (s)'), ax.set_ylabel('Real part'), ax.set_zlabel('Imag part')
ax.set_title('Complex sine wave in all its 3D glory')
plt.show()


#exponencial de la función 2
print("Exponencial 2da señal")
csw=np.exp(sinewave2)
fig=plt.figure()
plt.plot(csw)
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Señal exponencial 2")
plt.legend(loc='best')
plt.show() 

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(time,np.real(csw),np.imag(csw))
ax.set_xlabel('Time (s)'), ax.set_ylabel('Real part'), ax.set_zlabel('Imag part')
ax.set_title('Complex sine wave in all its 3D glory')
plt.show()


# Producto punto x1(t)(.)x2(t)
srate=800;
time=np.arange(0.,0.25,1/srate)
freq1 = 25;    # frequency in Hz
amp = 2;    # amplitude in a.u. 
x1= amp*np.cos(2*np.pi*freq1*time)
freq2 = 75/2;    # frequency in Hz
amp = 2;    # amplitude in a.u. 
fase = np.pi;
x2= amp*np.cos(2*np.pi*freq2*time+fase)
# Grafica del prodcuto punto entre una señal gaussiana y x1(t)
srate = 1000;
time  = np.arange(-1.,1.,1./srate)
print("Producto punto resultante")
x1= amp*np.cos(2*np.pi*freq1*time)
gauss  = np.exp( (-time**2) / .1);
signal = np.multiply(x1,gauss)
sinefrex = np.arange(0.,25.,.5);
plt.show()

dps = np.zeros(len(sinefrex));
# bucle de las ondas sinusoidales
for fi in range(1,len(dps)):
    # crear la señal sinusoidal
    sinew = np.sin( 2*np.pi*sinefrex[fi]*time) 
    # compute dot product
    dps[fi] = np.dot(sinew,signal ) / len(time)
# and plot
plt.stem(sinefrex,dps)

dp = sum(np.multiply(x1,x2))
print('dp es:',dp)







 
