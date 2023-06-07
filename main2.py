import serial
import pandas as pd
import csv 
import time 
import numpy as np

#constantes
path=r"parameters\rango.csv"
rango = pd.read_csv(path)
arduino_port = 'COM8'  # Cambia esto al puerto serial correcto en tu computadora
baud_rate = 9600



#funcion de clasificacion de la letra 
def traduccion(line,rango):
    test=[[],[],[],[],[]]
    columns = rango.columns
    for i in range(len(rango.index)):
            if rango.loc[i,"THUMB_MIN"]<=line[0]<= rango.loc[i,"THUMB_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
            if rango.loc[i,"INDEX_MIN"]<=line[1]<= rango.loc[i,"INDEX_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
            if rango.loc[i,"MIDDLE_MIN"]<=line[2]<= rango.loc[i,"MIDDLE_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
            if rango.loc[i,"HEART_MIN"]<=line[3]<= rango.loc[i,"HEART_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
            if rango.loc[i,"PINKY_MIN"]<=line[4]<= rango.loc[i,"PINKY_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
            if rango.loc[i,"X_MIN"]<=line[5]<= rango.loc[i,"X_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
            if rango.loc[i,"Y_MIN"]<=line[6]<= rango.loc[i,"Y_MAX"]:
                test[i].append(rango.loc[i,"LETTER"])
    return test

ser = serial.Serial(arduino_port, baud_rate) 
line = ser.readline().decode('utf-8').strip()
line=line.split("\t")
line = [float(x) for x in line]  # Convert the values to integers
line = [int(x) for x in line]
print(line)
test=traduccion(line,rango)
print(test)
lista_mas_larga = max(test, key=len)
print("la letra es: ", lista_mas_larga[0])             