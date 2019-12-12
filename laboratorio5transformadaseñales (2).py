# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:32:14 2019

@author: DANIEL
"""
#LABORATORIO 5: TRANFORMADA DE FOURIER DE SEÑALES
#LIBRERIAS
import signals as sigs
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal
from scipy.ndimage import gaussian_filter
import math

def calc_dft(sig_src_arr):
    sig_dest_imx_arr = [None]*int((len(sig_src_arr)/2))
    sig_dest_rex_arr = [None]*int((len(sig_src_arr)/2))
    sig_dest_mag_arr = [None]*int((len(sig_src_arr)/2))
    
    for j in range(int(len(sig_src_arr)/2)):
        sig_dest_rex_arr[j] =0
        sig_dest_imx_arr[j] =0

    for k in range(int(len(sig_src_arr)/2)):
        for i in range(len(sig_src_arr)):
            sig_dest_rex_arr[k] = sig_dest_rex_arr[k] + sig_src_arr[i]*math.cos(2*math.pi*k*i/len(sig_src_arr))
            sig_dest_imx_arr[k] = sig_dest_imx_arr[k] - sig_src_arr[i]*math.sin(2*math.pi*k*i/len(sig_src_arr))

    for x in range(int(len(sig_src_arr)/2)):
        sig_dest_mag_arr[x] = math.sqrt(math.pow(sig_dest_rex_arr[x],2)+math.pow(sig_dest_imx_arr[x],2))
        
    style.use('ggplot')
    f,plt_arr = plt.subplots(1, sharex=True)
    f.suptitle("Discrete Fourier Transform (DFT)")


    #plt_arr[0].plot(sig_src_arr, color='red')
    #plt_arr[0].set_title("Input Signal",color='red')
    
    #plt_arr[1].plot(sig_dest_rex_arr, color='green')
    #plt_arr[1].set_title("Frequency Domain(Real part)",color='green')

    #plt_arr[2].plot(sig_dest_imx_arr, color='green')
    #plt_arr[2].set_title("Frequency Domain(Imaginary part)",color='green')

    #plt_arr[3].plot(sig_dest_mag_arr, color='magenta')
    #plt_arr[3].set_title("Frequency Domain (Magnitude))",color='magenta')

    plt.xlim(0,15)
    #plt.ylim(0,1000)
    plt.stem(sig_dest_mag_arr)
    
calc_dft(sigs.ruido_1KHz)
calc_dft(sigs.ruido_100Hz)
calc_dft(sigs.ruido_extra_100Hz)
calc_dft(sigs.ecg_100Hz)
calc_dft(sigs.airflow_calibrated_100Hz)
calc_dft(sigs.airflow_100Hz)

#####################suavizado de una señal ruido_1KHz ##########################

savis_smooth= signal.savgol_filter(sigs.ruido_1KHz,25,3) ### señal de entrada, tamaño de Wi, exponente
signal.savgol_coeffs(15,10)
plt.plot(savis_smooth,color='blue',label='data smoothing')
plt.plot(sigs.ruido_1KHz,color='red',label='original samples')
plt.title('Savistky-Golay')
plt.grid(True,color='black',linestyle='--')
plt.show()

gaus_smooth=gaussian_filter(sigs.ruido_1KHz,20)
plt.plot(gaus_smooth,color='blue',label='data smoothing')
plt.plot(sigs.ruido_1KHz,color='red',label='original samples')
plt.title('GAUSSIAN SMOOTH ')
plt.grid(True,color='black',linestyle='--')
plt.show()
##################### componentes de ruido en la señal  ruido_1KHz ##########
ruido=sigs.ruido_1KHz-savis_smooth
ruido
plt.plot(ruido,'c')
plt.ylabel('tiempo')
plt.xlabel('magnitud')
plt.title ('Ruido filtro')
plt.grid(True,color='black',linestyle='--')
plt.show()

plt.xlim(0,15)
plt.stem(ruido)
plt.title ('Componentes de Ruido')
plt.grid(True,color='black',linestyle='--')
plt.show()
##################componentes en la señal original################################
plt.xlim(0,25)
#plt.ylim(0,1000)
plt.stem(sigs.ruido_1KHz)
plt.title('componentes en señal original')
plt.grid(True,color='black',linestyle='--')
plt.show()
#####################suavizado de una señal de ruido_100Hz ##########################
savis_smooth1= signal.savgol_filter(sigs.ruido_100Hz,11,3) ### señal de entrada, tamaño de Wi, exponente
signal.savgol_coeffs(11,3)
plt.plot(savis_smooth1,color='blue',label='data smoothing')
plt.plot(sigs.ruido_100Hz,color='red',label='original samples')
plt.title('Savistky-Golay')
plt.grid(True,color='black',linestyle='--')
plt.show()

gaus_smooth1=gaussian_filter(sigs.ruido_100Hz,12)
plt.plot(gaus_smooth1,color='blue',label='data smoothing')
plt.plot(sigs.ruido_100Hz,color='red',label='original samples')
plt.title('GAUSSIAN SMOOTH ')
plt.grid(True,color='black',linestyle='--')
plt.show()

##################### componentes de ruido en la señal ruido_1KHz ##########
ruido1=sigs.ruido_100Hz-savis_smooth1
ruido1
plt.plot(ruido1,'c')
plt.ylabel('tiempo')
plt.xlabel('magnitud')
plt.title ('Ruido filtro')
plt.grid(True,color='black',linestyle='--')
plt.show()
plt.xlim(0,15)
plt.stem(ruido1)
plt.title ('Componentes de Ruido')
plt.grid(True,color='black',linestyle='--')
plt.show()
##################componentes en la señal original################################
plt.xlim(0,25)
#plt.ylim(0,1000)
plt.stem(sigs.ruido_100Hz)
plt.title('componentes en señal original')
plt.grid(True,color='black',linestyle='--')
plt.show()
 
#####################suavizado de una señal ruido_extra_100Hz##########################
savis_smooth2= signal.savgol_filter(sigs.ruido_extra_100Hz,11,3) ### señal de entrada, tamaño de Wi, exponente
signal.savgol_coeffs(11,3)
plt.plot(savis_smooth2,color='blue',label='data smoothing')
plt.plot(sigs.ruido_extra_100Hz,color='red',label='original samples')
plt.title('Savistky-Golay')
plt.grid(True,color='black',linestyle='--')
plt.show()

gaus_smooth=gaussian_filter(sigs.ruido_extra_100Hz,12)
plt.plot(gaus_smooth,color='blue',label='data smoothing')
plt.plot(sigs.ruido_extra_100Hz,color='red',label='original samples')
plt.title('GAUSSIAN SMOOTH ')
plt.grid(True,color='black',linestyle='--')
plt.show()

##################### componentes de ruido en la señal ruido_extra_100Hz ##########
ruido2=sigs.ruido_extra_100Hz-savis_smooth2
ruido2
plt.plot(ruido2,'c')
plt.ylabel('tiempo')
plt.xlabel('magnitud')
plt.title ('Ruido filtro')
plt.grid(True,color='black',linestyle='--')
plt.show()
plt.xlim(0,15)
plt.stem(ruido2)
plt.title ('Componentes de Ruido')
plt.grid(True,color='black',linestyle='--')
plt.show()
 ##################componentes en la señal original################################
plt.xlim(0,25)
#plt.ylim(0,1000)
plt.stem(sigs.ruido_extra_100Hz)
plt.title('componentes en señal original')
plt.grid(True,color='black',linestyle='--')
plt.show()
#####################suavizado de una señal ecg_100Hz #########################
savis_smooth3= signal.savgol_filter(sigs.ecg_100Hz,11,3) ### señal de entrada, tamaño de Wi, exponente
signal.savgol_coeffs(11,3)
plt.plot(savis_smooth3,color='blue',label='data smoothing')
plt.plot(sigs.ecg_100Hz,color='red',label='original samples')
plt.title('Savistky-Golay')
plt.grid(True,color='black',linestyle='--')
plt.show()

gaus_smooth=gaussian_filter(sigs.ecg_100Hz,12)
plt.plot(gaus_smooth,color='blue',label='data smoothing')
plt.plot(sigs.ecg_100Hz,color='red',label='original samples')
plt.title('GAUSSIAN SMOOTH ')
plt.grid(True,color='black',linestyle='--')
plt.show()

##################### componentes de ruido en la señal ##########
ruido3=sigs.ecg_100Hz-savis_smooth3
ruido3
plt.plot(ruido3,'c')
plt.ylabel('tiempo')
plt.xlabel('magnitud')
plt.title ('Ruido filtro')
plt.grid(True,color='black',linestyle='--')
plt.show()
plt.xlim(0,15)
plt.stem(ruido3)
plt.title ('Componentes de Ruido')
plt.grid(True,color='black',linestyle='--')
plt.show()
##################componentes en la señal original################################
plt.xlim(0,25)
#plt.ylim(0,1000)
plt.stem(sigs.ecg_100Hz)
plt.title('componentes en señal original')
plt.grid(True,color='black',linestyle='--')
plt.show()
#####################suavizado de una señal airflow_calibrated_100Hz ########################
savis_smooth4= signal.savgol_filter(sigs.airflow_calibrated_100Hz,11,3) ### señal de entrada, tamaño de Wi, exponente
signal.savgol_coeffs(11,3)
plt.plot(savis_smooth4,color='blue',label='data smoothing')
plt.plot(sigs.airflow_calibrated_100Hz,color='red',label='original samples')
plt.title('Savistky-Golay')
plt.grid(True,color='black',linestyle='--')
plt.show()

gaus_smooth=gaussian_filter(sigs.airflow_calibrated_100Hz,12)
plt.plot(gaus_smooth,color='blue',label='data smoothing')
plt.plot(sigs.airflow_calibrated_100Hz,color='red',label='original samples')
plt.title('GAUSSIAN SMOOTH ')
plt.grid(True,color='black',linestyle='--')
plt.show()

##################### componentes de ruido en la señal ##########
ruido4=sigs.airflow_calibrated_100Hz-savis_smooth4
ruido4
plt.plot(ruido4,'c')
plt.ylabel('tiempo')
plt.xlabel('magnitud')
plt.title ('Ruido filtro')
plt.grid(True,color='black',linestyle='--')
plt.show()
plt.xlim(0,15)
plt.stem(ruido4)
plt.title ('Componentes de Ruido')
plt.grid(True,color='black',linestyle='--')
plt.show()
##################componentes en la señal original################################
plt.xlim(0,25)
#plt.ylim(0,1000)
plt.stem(sigs.airflow_calibrated_100Hz)
plt.title('componentes en señal original')
plt.grid(True,color='black',linestyle='--')
plt.show()
 
#####################suavizado de una señal airflow_100Hz #########################
savis_smooth5= signal.savgol_filter(sigs.airflow_100Hz,11,3) ### señal de entrada, tamaño de Wi, exponente
signal.savgol_coeffs(11,3)
plt.plot(savis_smooth5,color='blue',label='data smoothing')
plt.plot(sigs.airflow_100Hz,color='red',label='original samples')
plt.title('Savistky-Golay')
plt.grid(True,color='black',linestyle='--')
plt.show()

gaus_smooth=gaussian_filter(sigs.airflow_100Hz,12)
plt.plot(gaus_smooth,color='blue',label='data smoothing')
plt.plot(sigs.airflow_100Hz,color='red',label='original samples')
plt.title('GAUSSIAN SMOOTH ')
plt.grid(True,color='black',linestyle='--')
plt.show()

##################### componentes de ruido en la señal ##########
ruido5=sigs.airflow_100Hz-savis_smooth5
ruido5
plt.plot(ruido5,'c')
plt.ylabel('tiempo')
plt.xlabel('magnitud')
plt.title ('Ruido filtro')
plt.grid(True,color='black',linestyle='--')
plt.show()
plt.xlim(0,15)
plt.stem(ruido5)
plt.title ('Componentes de Ruido')
plt.grid(True,color='black',linestyle='--')
plt.show()
##################componentes en la señal original################################
plt.xlim(0,25)
#plt.ylim(0,1000)
plt.stem(sigs.airflow_100Hz)
plt.title('componentes en señal original')
plt.grid(True,color='black',linestyle='--')
plt.show()
 
 