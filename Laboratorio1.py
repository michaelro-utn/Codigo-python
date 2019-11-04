# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:31:34 2019

@author: Michael Rodriguez
"""
import numpy as np
import pylab as plt

#####Señal nº1 #########
 
#x1(t)=4cos(t)
#generar muestras
#periodo >5
muestras=np.arange(0,8,1/100)
muestras
#Parámetros
amp1=4
freq1=(1/2)*(1/np.pi)
fase1=0
#generar señal 1
x1=amp1*np.cos(2*np.pi*freq1*muestras)
#Imprimir la señal mediante comando plt.plot
plt.plot(x1,color='red')
plt.title("Señal continua 4cos(t)")
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.grid()
plt.show()

## Señal N° 2 ###
## x2(t)=4cos(6t)
#generar muestras
t2=np.arange(0,3,1/100)
t2
#definir parametros 
amp2=4# amplitud 
frec2=3/np.pi# frecuencia=3/pi
fase2=0# fase
#generar señal
x2=amp2*np.cos(2*np.pi*frec2*t2)
#graficar señal
plt.plot(x2, label="4cos(6t)",color='red')
#Titutlo eje x
plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Voltios")
#titulo de grafica
plt.title("Señal continua sinosuidal numero 2")
#leyenda al grafico
plt.legend(loc='best')
#cuadricula
plt.grid()
#muestre la grafica
plt.show()

####### Señal nº3 ########☻
#x2=4cos(6t+pi)
#generar muestas
muestra1=np.arange(0,1,1/100)
muestra1
#Parámetros
amp3=4
freq3=3*np.pi
fase3=np.pi
#generar señal 2
x3=4*np.cos(2*np.pi*freq3*muestra1)
#Imprimir la señal mediante comando plt.plot
plt.plot(x3, color='magenta')
plt.title("Señal continua 4cos(6t+pi)")
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.grid()
plt.show()

## Señal N°4 ###
## x4(t)= 4cos(6t+pi)+3sin(5t+(2*pi)/3)###

#generar muestras primera parte de la señal 4cos(6t+pi)  
t41=np.arange(0,5,1/100)
t41
#definir parametros 
amp41=4# amplitud 
frec41=3/np.pi# frecuencia=3/pi
fase41=np.pi  # fase
#generar señal
x41=amp41*np.cos(2*np.pi*frec41*t41+fase41)
#generar muestras segunda parte de la señal 3sin(5t+(2*pi)/3) 
t42=np.arange(0,5,1/100)
t42
#definir parametros 
amp42=3# amplitud 
frec42=5/(2*np.pi)# frecuencia=3/pi
fase42=(2*np.pi)/3# fase
#generar señal
x42=amp42*np.sin(2*np.pi*frec42*t42+fase42)
#grafica de la funcion por separado

#grafica primara parte de la funcion
plt.plot(x41, label="4cos(6t+pi)",color='blue')
#grafica segunda parte  de la funcion
plt.plot(x42, label="3sin(5t+(2*pi)/3)",color='green')
#Titutlo eje x
plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Voltios")
#titulo de grafica
plt.title("Señal numero 4: compleja continua sinosuida l")
#leyenda al grafico
plt.legend(loc='best')
#cuadricula
plt.grid()
#muestre la grafica
plt.show()

### grafica de la funcion x4(t)= 4cos(6t+pi)+3sin(5t+(2*pi)/3) completa
## generar funcion completa 
xt=x41+x42
## grafica de la funcion completa
plt.plot(xt, label="xt=4cos(6t+pi)+3sin(5t+(2*pi)/3)",color='cyan')
#Titutlo eje x
plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Voltios")
#titulo de grafica
plt.title("Señal numero 4: total continua sinosuidal")
#leyenda al grafico
plt.legend(loc='best')
#cuadricula
plt.grid()
#muestre la grafica
plt.show()

####Señal nº5 #######
#x(n)=2sin(n), n=100
#Parámetros
amp5=2
freq5=1/(2*np.pi)
#componentes de n en frecuencia con periodo >6
n=np.linspace(0,13*np.pi*freq5,100)
#generar señal
x5=amp5*np.sin(n)
#Imprimir señal discreta mediante el comando stem
plt.stem(n,x5,'g',use_line_collection=True)
plt.title("Señal discreta 2sin(n)")
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.grid()
plt.show()



#### Comprobación postulado A2 ####

#Impresión señal original 
plt.plot(x3, label= 'Señal original',color= 'cyan' )
plt.title("Función x3(t) original ") #titulo función
plt.xlabel("Tiempo") #Nombre eje X
plt.ylabel("Voltios") #nombre eje Y
#Generar señal con frecuencia variada
freq6=12*np.pi #nueva frecuencia a comparar
x6=4*np.cos(2*np.pi*freq6*muestra1)
#Imprimir señal con nueva frecuencia 
plt.plot(x6, label='Señal nueva' ,color= 'black')
plt.title("Función x3(t) con nueva frecuencia") #titulo función 
plt.xlabel("Tiempo") #Nombre eje x
plt.ylabel("Voltios") #Nombre eje Y 
plt.title("Comprobación postulado A2")
plt.legend(loc='best') #Identificación de señales
plt.grid()
plt.show()

#### Comprobacion postulado A3 ######
## x2(t)=4cos(6t)
#generar muestras
tp=np.arange(0,1,1/50)
tp
#definir parametros 
ampli=4# amplitud 

##frecuencias de prueba###
frecue1=2
frecue2=0
frecue3=5
#generar señales
x21=ampli*np.cos(2*np.pi*frecue1*tp)# señal con frecuencia baja aumenta el periodo
x22=ampli*np.cos(2*np.pi*frecue2*tp)#señal con frecuncia cero el periodo es infinito
x23=ampli*np.cos(2*np.pi*frecue3*tp)# señal con frecuencia alta disminuye el periodo
#grafica de señal con frecuenca de 10
plt.plot(x21, label="4cos(6t)",color='red')
# grafica de señal con frecuencia 0
plt.plot(x22, label="4cos(6t)",color='blue')
#grafica de señal con frecuencia de 80
plt.plot(x23, label="4cos(6t)",color='green')
#Titutlo eje x
plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Voltios")
#titulo de grafica
plt.title("Demostracion postulado A3 en una señal continua senosuidal")
#leyenda al grafico
plt.legend(loc='best')
#cuadricula
plt.grid()
#muestre la grafica
plt.show()


#### Comprobación postulado B2 ######
#x7=2sin(6n)
#generar parámetros
amp7=2
freq7=3/np.pi
freq8=8/np.pi
#componentes de n en frecuencia 
n7=np.linspace(0,2*np.pi*freq7,30)
n8=np.linspace(0,0.8*np.pi*freq8,50) #Función discreta con una frecuencia multiplo de 2pi
#generar función discreta
x7=amp7*np.sin(n7)
x8=amp7*np.sin(n8)
#Imprimir funcion discreta 
plt.stem(n7,x7,'m',use_line_collection=True,label='Frecuencia 3/pi')
plt.stem(n8,x8,'c',use_line_collection=True, label=' Frecuencia 12/pi')
plt.legend(loc='best')
plt.title("Comprobación postulado B2")
plt.show()

#### Comprobacion postulado B3 #####

##señal nº1
#s1=3sin(8n)
#generar parámetros
am=3
fr1=8/np.pi
#componentes de n en frecuencia 
n10=np.linspace(0,1*np.pi*fr1,45)
#generar señal discreta 
s1=am*np.sin(n10)
#imprimir señal discreta nº1 
plt.stem(n10,s1,'g',use_line_collection=True, label='Señal 1, frecuencia<5')

##señal nº2
#s2=7cos(10n)
#generar parámetros
am2=7
fr2=10/np.pi
#componentes en n frecuencia
n11=np.linspace(0,1*np.pi*fr2,45)
#generar señal discreta nº2
s2=am2*np.sin(n11)
#Imprimir señal discreta nº2
plt.stem(n11,s2,'y',use_line_collection=True,label='Señal 2, frecuencia<5')

##señal nº3
#s3=2sin(10pi*n)
am3=2
fr3=(10*np.pi)/(2*np.pi)
#Componentes en n frecuencias 
n12=np.linspace(0,1*np.pi*fr3,45)
#generar señal discreta nº3
s3=am3*np.sin(n12)
#imprimir señal discreta nº3
plt.stem(n12,s3,'m',use_line_collection=True,label='Señal 3,frecuencia=3')

#Señal nº4
#s4=8sin(13pi*n)
#generar parámetros
am4=8
fr4=(13*np.pi)/(2*np.pi)
#componentes en n frecuencia 
n13=np.linspace(0,1*np.pi*fr4,45)
#generar señal discreta nº4
s4=am4*np.sin(n13)
#imprimir señal discreta nº4
plt.stem(n13,s4,'c',use_line_collection=True,label='Señal 4 ,5<frecuencia<10')

#señal nº5
#s5=4sin(17pi*n)
#generar parámetros
am5=4
fr5=(17*np.pi)/(2*np.pi)
#componentes de n en frecuencia 
n14=np.linspace(0,1*np.pi*fr5,45)
#generar señal discreta nº5
s5=am5*np.sin(n14)
#imprimir señal discreta nº5
plt.stem(n14,s5,'b',use_line_collection=True, label='Señal 5,5<frecuencia<10')
plt.legend(loc='best')
plt.title("Comprobación postulado B3")
plt.grid()
plt.show()

