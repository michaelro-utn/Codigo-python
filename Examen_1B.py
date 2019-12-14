# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:42:37 2019

@author: Michae
"""

import signals as sigs
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

##señal de ruido 1KHz
print("##UNIVERISDAD TÉCNICA DEL NORTE##")
print("##Examen Procesamiento Digital de señales##")
print("#Michael Rodríguez")
print("########################")
print("Running Sum")
print("########################")
a = sigs.ruido_1KHz
#print (a)
print("##Señal de ruido original a 1KHz##")
plt.plot(a)
plt.title("Señal ruido 1KHz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("Suma acumulativa")
b = [sum(a[:(i+1)]) for i, j in enumerate(a)]
#print(b)
plt.plot(b,'c')
plt.title("Señal Acumulada (Ruido 1KHz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal de ruido 100Hz
c = sigs.ruido_100Hz
print("##Señal de ruido 100Hz##")
#print (a)
plt.plot(c,'y')
plt.title("Señal ruido 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print("Suma acumulativa")
series=pd.Series(c)
cumsum=series.cumsum(skipna= False)
cumsum
plt.plot(cumsum,'r')
plt.title("Señal Acumulada (Ruido 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal de ruido extra 100Hz
d = sigs.ruido_extra_100Hz
#print (d)
print("##Señal de ruido original extra 100KHz##")
plt.plot(d)
plt.title("Señal ruido extra 100KHz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("Suma acumulativa")
e = [sum(a[:(i+1)]) for i, j in enumerate(a)]
#print(b)
plt.plot(e,'c')
plt.title("Señal Acumulada (Ruido extra 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal ecg a 100Hz
ecg1 = sigs.ecg_100Hz
print("##Señal de ecg 100Hz##")
#print (a)
plt.plot(ecg1,'g')
plt.title("Señal ecg 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print("Suma acumulativa")
series1=pd.Series(ecg1)
cumsum1=series1.cumsum(skipna= False)
cumsum1
plt.plot(cumsum1,'b')
plt.title("Señal Acumulada (ecg 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal airflow calibrated 100Hz
afw = sigs.airflow_calibrated_100Hz
print("##Señal airflow calibrated 100Hz##")
#print (a)
plt.plot(afw,'b')
plt.title("Señal airflow calibrated 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print("Suma acumulativa")
series2=pd.Series(afw)
cumsum2=series2.cumsum(skipna= False)
cumsum2
plt.plot(cumsum2,'y')
plt.title("Señal Acumulada (airflow calibrated 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal airflow 100Hz
afw1 = sigs.airflow_100Hz
print("##Señal airflow_100Hz##")
#print (a)
plt.plot(afw1,'m')
plt.title("Señal airflow_100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print("Suma acumulativa")
series3=pd.Series(afw1)
cumsum3=series3.cumsum(skipna= False)
cumsum3
plt.plot(cumsum3,'b')
plt.title("Señal Acumulada (airflow_100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

###First Difference 
print("########################")
print("first Difference")
print("########################")
ad = sigs.ruido_1KHz
#print (a)
print("##Señal de ruido original a 1KHz##")
plt.plot(ad)
plt.title("Señal ruido 1KHz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("First Difference")
ffd=np.diff(ad)
plt.plot(ffd,'r')
plt.title("First difference(Señal ruido  1KHz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

#Señal de ruido 100Hz
ad1 = sigs.ruido_100Hz
#print (a)
print("##Señal de ruido original a 100Hz##")
plt.plot(ad1,'c')
plt.title("Señal ruido 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("First Difference")
ffd1=np.diff(ad)
plt.plot(ffd1,'b')
plt.title("First difference(Señal ruido 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

#Señal de ruido extra 100Hz
ad2 = sigs.ruido_extra_100Hz
#print (a)
print("##Señal de ruido original extra 100Hz##")
plt.plot(ad2,'y')
plt.title("Señal ruido extra 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("First Difference")
ffd2=np.diff(ad2)
plt.plot(ffd2,'m')
plt.title("First difference(Señal ruido extra 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

#Señal ecg 100 Hz
ad3 = sigs.ecg_100Hz
#print (a)
print("##Señal ecg 100Hz##")
plt.plot(ad3,'r')
plt.title("Señal ecg 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("First Difference")
ffd3=np.diff(ad3)
plt.plot(ffd3,'g')
plt.title("First difference(Señal ecg 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal airflow calibrated 100Hz
ad4 = sigs.airflow_calibrated_100Hz
#print (a)
print("##Señal airflow calibrated 100Hz##")
plt.plot(ad4,'c')
plt.title("Señal airflow calibrated 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("First Difference")
ffd4=np.diff(ad4)
plt.plot(ffd4,'y')
plt.title("First difference(Señal airflow calibrated 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()

##Señal airflow 100Hz
ad5 = sigs.airflow_100Hz
#print (a)
print("##Señal airflow  100Hz##")
plt.plot(ad5,'b')
plt.title("Señal airflow 100Hz")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
print ("First Difference")
ffd5=np.diff(ad5)
plt.plot(ffd5,'m')
plt.title("First difference(Señal airflow 100Hz)")
plt.xlabel("Tiempo (T)")
plt.ylabel("Voltaje(V)")
plt.grid()
plt.show()
