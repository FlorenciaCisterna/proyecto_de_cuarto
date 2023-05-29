import serial
import pandas as pd
import csv 


path="parameters/"

# Set up the serial port
for j in range(5):
    letter=str(input("ingrese letra: "))
    ser = serial.Serial('COM6', 9600)  # Replace 'COM3' with the name of the serial port on your computer
    list=[]
    # Read data from Arduino
    for i in range (60):
        line = ser.readline().decode('utf-8').strip()
        line=line.split("\t")
        line = [int(x) for x in line]  # Convert the values to integers
        list.append(line)
        print(str(i),line)
        
    list=pd.DataFrame(list)
    list.columns=["THUMB","INDEX","MIDDLE","HEART","PINKY","ACCELERATION"]
    list['LETTER']=letter
    list.to_csv(path+letter+".csv", index=False)
    print(list)