# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 07:55:37 2019

@author: Michae
"""

import numpy as np
import pylab as plt

#####EJERCICIO N1#######
#######################
ampli1=2# amplitud de la señal 
frecue1=(60*np.pi)/(2*np.pi)# frecuencia= 30 Hz
frecue1
#el timepo de una sola oscilacion  es 1/30
#timepo minimo y maximo
tmin=-0.0333
tmax=0.0333
#se define el timepo de la señal
tiempo1=np.linspace(tmin,tmax,400)
tiempo1
#generar señal de muestreo
x1a=ampli1*np.cos(2*np.pi*frecue1*tiempo1)
#graficar señal
plt.plot(tiempo1,x1a, label="2cos(60pit)",color='cyan')
#Frecuencia de muestreo de la señal
# en este caso, estamos usando la tasa Nyquist.
#Periodo de muestreo
FM1 = 1 / (2 * frecue1)
#Tiempo minimo
nmin1a = np.ceil (tmin / FM1)
#Tiempo maximo
nmax1a = np.floor (tmax / FM1)
#Tiempo de la señal.
n1a = np.arange (nmin1a, nmax1a)
#Señal a la velocidad de muestreo
x11a = ampli1*np.cos (2 * np.pi *frecue1* n1a * FM1) 
#Se grafica la señal.
plt.plot (n1a * FM1, x11a, 'b.')
plt.title("Muestreo de Señal a 2B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.show()
#  muestreo 4B
FM2 = 1 / (4 * frecue1)
#Tiempo minimo
nmin2a = np.ceil (tmin / FM2)
#Tiempo maximo
nmax2a = np.floor (tmax / FM2)
#Tiempo de la señal.
n2a = np.arange (nmin2a, nmax2a)
#Señal a la velocidad de muestreo
x12a = ampli1*np.cos (2 * np.pi *frecue1* n2a * FM2) 
#Se grafica la señal.
plt.plot(tiempo1,x1a, label="2cos(60pit)",color='cyan')
plt.plot (n2a * FM2, x12a, 'r.')
plt.title("Muestreo de Señal a 4B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.show()

## Muestreo 6B
FM3 = 1 / (6 * frecue1)
#Tiempo minimo
nmin3a = np.ceil (tmin / FM3)
#Tiempo maximo
nmax3a = np.floor (tmax / FM3)
#Tiempo de la señal.
n3a = np.arange (nmin3a, nmax3a)
#Señal a la velocidad de muestreo
x13a = ampli1*np.cos (2 * np.pi *frecue1* n3a * FM3) 
#Se grafica la señal.
plt.plot(tiempo1,x1a, label="2cos(60pit)",color='cyan')
plt.plot (n3a * FM3, x13a, '.')
plt.title("Muestreo de Señal a 6B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.show()


####EJERCICIO N2#########
########################
#Parametros de la señal
f=30
f1=40
f2=45
amp=2
#El tiempo mínimo que necesita una función para oscilar una vez T=1/45=0.25
tmin=-0.02
tmax=0.02
#
t=np.linspace(tmin,tmax,400)
#definir la señal de muestreo
x2=(amp*np.cos(2*np.pi*f*t))+(amp*np.cos(2*np.pi*f1*t))+(amp*np.cos(2*np.pi*f2*t))
#graficar la señal
plt.plot(t,x2,color="cyan")
plt.title("Muestreo de Señal a B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()


#definir periodo de muestreo
T=1/(2*f2)
#tiempos de la gráfica 
#ceil: aproxima la decimal mas bajo
nmin=np.ceil(tmin/T)
#floor:aproxima al decimal mas alto 
nmax=np.floor(tmax/T)

#muestras de la señal
n=np.arange(nmin,nmax)
#señal de muestreo
x1=(amp*np.cos(2*np.pi*f*n*T))+(amp*np.cos(2*np.pi*f1*n*T))+(amp*np.cos(2*np.pi*f2*n*T))
#graficar la señal
plt.plot(n*T,x1,'m.')#m.=magenta points 
plt.show()

##muestro de la señal a 2B## 

#definir periodo de muestreo
T2b=1/(4*f2)
#tiempos de la gráfica 
#ceil: aproxima la decimal mas bajo
nmin2b=np.ceil(tmin/T2b)
#floor:aproxima al decimal mas alto 
nmax2b=np.floor(tmax/T2b)

#muestras de la señal
n2b=np.arange(nmin2b,nmax2b)
#señal de muestreo
x2b=(amp*np.cos(2*np.pi*f*n2b*T2b))+(amp*np.cos(2*np.pi*f1*n2b*T2b))+(amp*np.cos(2*np.pi*f2*n2b*T2b))
#graficar la señal
plt.plot(t,x2,color="cyan")
plt.title("Muestreo de Señal a 2B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.plot(n2b*T2b,x2b,'m.')#m.=magenta points 
plt.show()

##muestreo señal a 4B##

#definir periodo de muestreo
T4b=1/(8*f2)
#tiempos de la gráfica 
#ceil: aproxima la decimal mas bajo
nmin4b=np.ceil(tmin/T4b)
#floor:aproxima al decimal mas alto 
nmax4b=np.floor(tmax/T4b)

#muestras de la señal
n4b=np.arange(nmin4b,nmax4b)
#señal de muestreo
x4b=(amp*np.cos(2*np.pi*f*n4b*T4b))+(amp*np.cos(2*np.pi*f1*n4b*T4b))+(amp*np.cos(2*np.pi*f2*n4b*T4b))
#graficar la señal
plt.plot(t,x2,color="cyan")
plt.title("Muestreo de Señal a 4B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.plot(n4b*T4b,x4b,'m.')#m.=magenta points 
plt.show()

###Muestreo señal 10B###
#definir periodo de muestreo
T10b=1/(64*f2)
#tiempos de la gráfica 
#ceil: aproxima la decimal mas bajo
nmin10b=np.ceil(tmin/T10b)
#floor:aproxima al decimal mas alto 
nmax10b=np.floor(tmax/T10b)

#muestras de la señal
n10b=np.arange(nmin10b,nmax10b)
#señal de muestreo
x10b=(amp*np.cos(2*np.pi*f*n10b*T10b))+(amp*np.cos(2*np.pi*f1*n10b*T10b))+(amp*np.cos(2*np.pi*f2*n10b*T10b))
#graficar la señal
plt.plot(t,x2,'c')
plt.plot(n10b*T10b,x10b,'m.')#m.=magenta points 
plt.title("Muestreo de Señal a 10B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.show()



########################
#EJERCICIO_3
########################

#Señal x(t)=2cos(600pit)+2cos(800pit)+2cos(900pit)

#Parametros de la señal
fr1=300
fr2=400
fr3=450
#El tiempo mínimo que necesita una función para oscilar una vez T=1/450=0.002

tmine3=-0.002
tmaxe3=0.002
#
te3=np.linspace(tmin,tmax,400)
#definir la señal de muestreo
xe3=(2*np.cos(2*np.pi*fr1*te3))+(2*np.cos(2*np.pi*fr2*te3))+(2*np.cos(2*np.pi*fr3*te3))
#graficar la señal
plt.plot(te3,xe3,'c')

#muestreo de la señal 
#definir periodo de muestreo
Te3=1/(2*fr3)
#tiempos de la gráfica 
#ceil: aproxima la decimal mas bajo
nmine3=np.ceil(tmine3/Te3)
#floor:aproxima al decimal mas alto 
nmaxe3=np.floor(tmaxe3/Te3)

#muestras de la señal
ne3=np.arange(nmine3,nmaxe3)
#señal de muestreo
x3t=(2*np.cos(2*np.pi*fr1*ne3*Te3))+(2*np.cos(2*np.pi*fr2*ne3*Te3))+(2*np.cos(2*np.pi*fr3*ne3*Te3))
#graficar la señal
plt.plot(ne3*Te3,x3t,'m.')#m.=magenta points 
plt.title("Muestreo señal a B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.show()

###Muestreo señal a 2B###
#Definir periodo muestral 
Te2b=1/(4*fr3)
#ceil: aproxima la decimal mas bajo
nmine2b=np.ceil(tmine3/Te2b)
#floor:aproxima al decimal mas alto 
nmaxe2b=np.floor(tmaxe3/Te2b)

#muestras de la señal
ne2b=np.arange(nmine2b,nmaxe2b)
#señal de muestreo
xe2b=(2*np.cos(2*np.pi*fr1*ne2b*Te2b))+(2*np.cos(2*np.pi*fr2*ne2b*Te2b))+(2*np.cos(2*np.pi*fr3*ne2b*Te2b))
#graficar la señal 
plt.plot(te3,xe3,'c')
plt.plot(ne2b*Te2b,xe2b,'m.')
plt.title("Muestreo de señal a 2B")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid()
plt.show()

###Muestreo de la señal a 4B### 
#Definir periodo muestral 
Te4b=1/(8*fr3)
#ceil: aproxima la decimal mas bajo
nmine4b=np.ceil(tmine3/Te4b)
#floor:aproxima al decimal mas alto 
nmaxe4b=np.floor(tmaxe3/Te4b)

#muestras de la señal
ne4b=np.arange(nmine4b,nmaxe4b)
#señal de muestreo
xe4b=(2*np.cos(2*np.pi*fr1*ne4b*Te4b))+(2*np.cos(2*np.pi*fr2*ne4b*Te4b))+(2*np.cos(2*np.pi*fr3*ne4b*Te4b))
#graficar la señal 
plt.plot(te3,xe3,'c')
plt.plot(ne4b*Te4b,xe4b,'m.')
plt.title("Muestreo de señal a 4B")
plt.ylabel("Voltaje")
plt.xlabel("Tiempo")
plt.grid()
plt.show()

####Muestreo de la señal a 10B###
#Definir periodo muestral 
Te10b=1/(64*fr3)
#ceil: aproxima la decimal mas bajo
nmine10b=np.ceil(tmine3/Te10b)
#floor:aproxima al decimal mas alto 
nmaxe10b=np.floor(tmaxe3/Te10b)

#muestras de la señal
ne10b=np.arange(nmine10b,nmaxe10b)
#señal de muestreo
xe10b=(2*np.cos(2*np.pi*fr1*ne10b*Te10b))+(2*np.cos(2*np.pi*fr2*ne10b*Te10b))+(2*np.cos(2*np.pi*fr3*ne10b*Te10b))
#graficar la señal 
plt.plot(te3,xe3,'c')
plt.plot(ne10b*Te10b,xe10b,'m.')
plt.title("Muestreo de señal a 4B")
plt.ylabel("Voltaje")
plt.xlabel("Tiempo")
plt.grid()
plt.show()




