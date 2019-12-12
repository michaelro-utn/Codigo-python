# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:38:32 2019

@author: Michae
"""

import numpy as np #libreria de formas matematicas 
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

##Señal1
def generar1():
    t=np.arange(0,5,1/100)
    num1=float(amp.get())
    num2=float(freq.get())    
    num3=float(phase.get())
    x=num1*np.cos((2*np.pi*num2*t)+num3)
    f=Figure(figsize=(2.5,2),dpi=100)
    img=f.add_subplot(111)
    img.plot(x,'c')
    canvas=FigureCanvasTkAgg(f,ventana) 
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=600,y=140)
    señal.set(float(amp.get())*np.cos((2*np.pi*float(freq.get())*t)+phase))
    amp.set("")
    freq.set("")
    phase.set("")

def muestrear1():
    tmin=-2
    tmax=2
    tiempo=np.linspace(tmin,tmax,200)
    num1=float(amp.get())
    num2=float(freq.get())    
    num3=float(phase.get())
    num4=float(muestra.get())
    x1=num1*np.cos((2*np.pi*num2*tiempo)+num3)
    FM=1/(num4*num2)
    nmin=np.ceil(tmin/FM)
    nmax=np.ceil(tmax/FM)
    n=np.arange(nmin,nmax)
    xm=num1*np.cos((2*np.pi*num2*n*FM)+num3)
    
    f1=Figure(figsize=(2.5,2),dpi=100)
    img=f1.add_subplot(111)
    img.plot(n*FM,xm,'b.')
    canvas=FigureCanvasTkAgg(f1,ventana) 
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=900,y=140)
    señal1.set(float(amp.get())*np.cos((2*np.pi*float(freq.get())*n*FM)+phase))
    amp.set("")
    freq.set("")
    phase.set("")
    muestra.set("")

###Señal 2
def generar2():
    t2=np.arange(0,5,1/100)
    num12=float(amp2.get())
    num22=float(freq2.get())    
    num32=float(phase2.get())
    x2=num12*np.cos((2*np.pi*num22*t2)+num32)
    f=Figure(figsize=(2.5,2),dpi=100)
    img=f.add_subplot(111)
    img.plot(x2,'m')
    canvas=FigureCanvasTkAgg(f,ventana) 
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=600,y=380)
    señal2.set(float(amp2.get())*np.cos((2*np.pi*float(freq2.get())*t2)+phase2))
    amp.set("")
    freq.set("")
    phase.set("")

def muestrear2():
    tmin2=-2
    tmax2=2
    tiempo2=np.linspace(tmin2,tmax2,200)
    num12=float(amp2.get())
    num22=float(freq2.get())    
    num32=float(phase2.get())
    num42=float(muestra2.get())
    
    x12=num12*np.cos((2*np.pi*num22*tiempo2)+num32)
    FM2=1/(num42*num22)
    nmin2=np.ceil(tmin2/FM2)
    nmax2=np.ceil(tmax2/FM2)
    n2=np.arange(nmin2,nmax2)
    xm2=num12*np.cos((2*np.pi*num22*n2*FM2)+num32)
    
    f12=Figure(figsize=(2.5,2),dpi=100)
    img=f12.add_subplot(111)
    img.plot(n2*FM2,xm2,'r.')
    canvas=FigureCanvasTkAgg(f12,ventana) 
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=900,y=380)
    señal12.set(float(amp2.get())*np.cos((2*np.pi*float(freq2.get())*n2*FM2)+phase2))
    amp2.set("")
    freq2.set("")
    phase2.set("")

def suma():
#primera señal
    t=np.arange(0,5,1/100)
    num1=float(amp.get())
    num2=float(freq.get())    
    num3=float(phase.get())
    xs=num1*np.cos((2*np.pi*num2*t)+num3)
#segunda señal
    t2=np.arange(0,5,1/100)
    num12=float(amp2.get())
    num22=float(freq2.get())    
    num32=float(phase2.get())
    x2s=num12*np.cos((2*np.pi*num22*t2)+num32)
    xt=xs+x2s    
    plt.plot(xt, label="xt=4cos(6t+pi)+3sin(5t+(2*pi)/3)",color='cyan')
    f=Figure(figsize=(2.5,2),dpi=100)
    img=f.add_subplot(111)
    img.plot(xt,'y')
    canvas=FigureCanvasTkAgg(f,ventana) 
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=150,y=452)
    señalt.set()
    amp.set("")
    freq.set("")
    phase.set("")

    
ventana=tk.Tk()
#parámetros señal1
amp=tk.StringVar()
freq=tk.StringVar()
phase=tk.StringVar()
x=tk.StringVar()
x1=tk.StringVar()
señal1=tk.StringVar()
#parámetros señal2 
amp2=tk.StringVar()
freq2=tk.StringVar()
phase2=tk.StringVar()
x2=tk.StringVar()
señal12=tk.StringVar()
señalt=tk.StringVar()
muestra=tk.StringVar()
muestra2=tk.StringVar()



ventana.title("Interfaz gráfica PDS")
#medidas de ventana 
ventana.geometry("1080x720")
ventana.configure(background='gray2')
etique1=tk.Label(ventana,text="UNIVERSIDAD TÉCNICA DEL NORTE",font=("Times New Roman",22),bg='gray2',fg='red2')
etique1.place(x=400,y=0)
etique2=tk.Label(ventana,text="FACULTAD DE INGENIERÍA EN CIENCIAS APLICADAS",font=("Times New Roman",12),bg='gray2',fg='snow')
etique2.place(x=450,y=40)
etique3=tk.Label(ventana,text="PROCESAMIENTO DIGITAL DE SEÑALES",font=("Times New Roman",12),bg='gray2',fg='snow')
etique3.place(x=490,y=60)
#Parámetros señal 1
etique4=tk.Label(ventana,text="Señal 1",font=("Arial",13),bg='gray2',fg='dodger blue')
etique4.place(x=10,y=110)
etique5=tk.Label(ventana,text="Amplitud ",font=("Arial",11),bg='gray2',fg='snow')
etique5.place(x=10,y=150)
entry1=tk.Entry(ventana,textvariable=amp)
entry1.place(x=10,y=180)
etique21=tk.Label(ventana,text="Muestra",font=("Arial",11),bg='gray2',fg='snow')
etique21.place(x=10,y=210)
entry21=tk.Entry(ventana,textvariable=muestra)
entry21.place(x=10,y=240)
etique6=tk.Label(ventana,text="Frecuencia",font=("Arial",11),bg='gray2',fg='snow')
etique6.place(x=150,y=150)
entry2=tk.Entry(ventana,textvariable=freq)
entry2.place(x=150,y=180)
etique7=tk.Label(ventana,text="Fase",font=("Arial",11),bg='gray2',fg='snow')
etique7.place(x=320,y=150)
entry3=tk.Entry(ventana,textvariable=phase)
entry3.place(x=320,y=180)
#Parámetros señal 2
etique8=tk.Label(ventana,text="Señal 2",font=("Arial",13),bg='gray2',fg='dodger blue')
etique8.place(x=10,y=340)
etique9=tk.Label(ventana,text="Amplitud",font=("Arial",11),bg='gray2',fg='snow')
etique9.place(x=10,y=380)
etique44=tk.Label(ventana,text="Muestra",font=("Arial",11),bg='gray2',fg='snow')
etique44.place(x=10,y=430)
entry44=tk.Entry(ventana,textvariable=muestra2)
entry44.place(x=10,y=450)
entry4=tk.Entry(ventana,textvariable=amp2)
entry4.place(x=10,y=400)
etique10=tk.Label(ventana,text="Frecuencia",font=("Arial",11),bg='gray2',fg='snow')
etique10.place(x=150,y=380)
entry5=tk.Entry(ventana,textvariable=freq2)
entry5.place(x=150,y=400)
etique11=tk.Label(ventana,text="Fase",font=("Arial",11),bg='gray2',fg='snow')
etique11.place(x=320,y=380)
entry6=tk.Entry(ventana,textvariable=phase2)
entry6.place(x=320,y=400)
etique12=tk.Label(ventana,text="Gráficos",font=("Arial",13),bg='gray2',fg='CadetBlue1')
etique12.place(x=840,y=100)

##Botones señal 1
boton1=tk.Button(ventana,text="Generar Señal 1",command=generar1)
boton1.place(x=460,y=150)
boton2=tk.Button(ventana,text="Muestreo Señal 1",command=muestrear1)
boton2.place(x=460,y=220)
##Botones señal 2
boton3=tk.Button(ventana,text="Generar señal 2",command=generar2)
boton3.place(x=460,y=380)
boton4=tk.Button(ventana,text="Muestrear señal 2",command=muestrear2)
boton4.place(x=460,y=450)
##boton suma
boton5=tk.Button(ventana,text="Sumar señales",command=suma)
boton5.place(x=460,y=520)


ventana.mainloop()