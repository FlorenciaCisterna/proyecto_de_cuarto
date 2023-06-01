import serial
import pandas as pd
import csv 
import time 

#constantes
path=r"parameters\rango.csv"
rango = pd.read_csv(path)
arduino_port = 'COM8'  # Cambia esto al puerto serial correcto en tu computadora
baud_rate = 9600


#funcion de clasificacion de la letra 
def traduccion(line,rango):
    for j in range(0,5):
        if rango.loc[j,"THUMB_MIN"]<=line[0]<=rango.loc[j,"THUMB_MAX"] and rango.loc[j,"INDEX_MIN"]<=line[1]<=rango.loc[j,"INDEX_MAX"] and rango.loc[j,"MIDDLE_MIN"]<=line[2]<=rango.loc[j,"MIDDLE_MAX"] and rango.loc[j,"HEART_MIN"]<=line[3]<=rango.loc[j,"HEART_MAX"] and rango.loc[j,"PINKY_MIN"]<=line[4]<=rango.loc[j,"PINKY_MAX"]:
            letter=rango.loc[j,"LETTER"]
            audio=rango.loc[j,"AUDIO"]
            print(letter)
            print(audio)
            return letter,audio
    print("No classification found")
    return None, None

#abre el puerto serial

ser = serial.Serial(arduino_port, baud_rate) 
 
#lee el puerto serial y clasifica su entrada y obtiene como salida la letra y su audio correspondiente
line = ser.readline().decode('utf-8').strip()
#line = ser.readline().decode('ascii').strip()
line=line.split("\t")
line = [int(x) for x in line]  # Convert the values to integers
print(line)
letter,audio=traduccion(line,rango)

#envio de datos al arduino
# Abre la comunicación serial con Arduino
#ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)
# Envía un número entero a Arduino
audio=str(audio)
ser.write(audio.encode())
ser.close()

