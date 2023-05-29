import serial
import pandas as pd
import csv 
import time 
path=r"parameters\rango.csv"
rango = pd.read_csv(path)

ser = serial.Serial('COM6', 9600)  # Replace 'COM3' with the name of the serial port on your computer
for i in range (0,10):
   
    line = ser.readline().decode('utf-8').strip()
    line=line.split("\t")
    line = [int(x) for x in line]  # Convert the values to integers
    print(line)
    if line[2]>400 and line[3]>400 and line[4]>400:
        if line[0]<200:
            if line[1]> rango.loc[0,"INDEX_MIN"]:
                print("A")
            elif rango.loc[1,"INDEX_MAX"]>line[1]>rango.loc[1,"INDEX_MIN"]:
                print("E")
            else:
                print("error en bloque 1")
        elif line[1]<200:
            print("I")
        else:
            print("error en  bloque 2")
    elif line[4]<100:
        if 100>line[1]>rango.loc[4,"INDEX_MIN"]:
            print("U")
        elif line[1]> rango.loc[3,"INDEX_MIN"]:
            print("O")
    else:
        print("error en bloque 3")
