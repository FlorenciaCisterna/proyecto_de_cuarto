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
    nada=1
    print("entra en la fc")
    if rango.loc[0,"MIDDLE_MIN"]<=line[2] and rango.loc[1,"HEART_MIN"]<=line[3] and rango.loc[1,"PINKY_MIN"]<=line[4]: #analiza los ultimos tres dedos, si estan en contraccion entra al bucle
        print("entra en el primer if de la fc")
        if line[7]<=0: #si la velocidad angular es negativa
            print("entra en LINE 7 Z NEGATIVO if de la fc")
            if rango.loc[1,"THUMB_MIN"]<=line[0]<=rango.loc[1,"THUMB_MAX"] and rango.loc[1,"INDEX_MIN"]<=line[1]<=rango.loc[1,"INDEX_MAX"] and line[7]<=0:
                print("LETRA E")
                letter=rango.loc[1,"LETTER"]
                audio=rango.loc[1,"AUDIO"]
                return letter, audio
        elif rango.loc[0,"X_MIN"]<=line[0]<=rango.loc[0,"X_MAX"]: #si la velocidad angular es positiva
            print("entra en ELIF X")
            if rango.loc[0,"INDEX_MIN"]<=line[1]<=rango.loc[0,"INDEX_MAX"] and rango.loc[0,"THUMB_MIN"]<=line[0]<=rango.loc[0,"THUMB_MAX"]:
                letter=rango.loc[0,"LETTER"]
                audio=rango.loc[0,"AUDIO"]
                return letter, audio
            elif rango.loc[2,"INDEX_MIN"]<=line[1]<=rango.loc[2,"INDEX_MAX"] and rango.loc[2,"THUMB_MIN"]<=line[0]<=rango.loc[2,"THUMB_MAX"]:
                letter=rango.loc[2,"LETTER"]
                audio=rango.loc[2,"AUDIO"]
                return letter, audio
            else:
                return nada, nada    
        else:
            return nada, nada 
    else:
        if  rango.loc[3,"INDEX_MIN"]<=line[1]<=rango.loc[3,"INDEX_MAX"] and line[7]<=0: 
            letter=rango.loc[3,"LETTER"]
            audio=rango.loc[3,"AUDIO"]
            return letter, audio 
        elif  rango.loc[4,"THUMB_MIN"]<=line[0]<=rango.loc[4,"THUMB_MAX"] and rango.loc[4,"INDEX_MIN"]<=line[1]<=rango.loc[4,"INDEX_MAX"]and rango.loc[4,"MIDDLE_MIN"]<=line[2]<=rango.loc[4,"MIDDLE_MAX"] and rango.loc[4,"HEART_MIN"]<=line[3]<=rango.loc[4,"HEART_MAX"] and rango.loc[4,"PINKY_MIN"]<=line[4] and line[7]>=0:       
            letter=rango.loc[4,"LETTER"]
            audio=rango.loc[4,"AUDIO"]
            return letter, audio 
        else:
            return nada, nada

#abre el puerto serial


while True : 
    ser = serial.Serial(arduino_port, baud_rate) 
    #lee el puerto serial y clasifica su entrada y obtiene como salida la letra y su audio correspondiente
    
    try:    
            line = ser.readline().decode('utf-8').strip()
            line=line.split("\t")
            line = [float(x) for x in line]  # Convert the values to integers
            print(line)
            line = [int(x) for x in line]
            print(line)
            letter, audio=traduccion(line,rango)
            if letter!=1:
                print(letter)
                audio=str(audio)
                ser.write(audio.encode())
                
            else:
                print("No classification found")
    except ValueError as e :
            print("Error: ",e)
           

    # Envía un número entero a Arduino
    time.sleep(2)
    ser.close()

