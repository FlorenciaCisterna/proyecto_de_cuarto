import serial
import pandas as pd
import csv 
# Set up the serial port
for j in range(5):
    print(j)
    letter=str(input("ingrese letra: "))
    ser = serial.Serial('COM8', 9600)  # Replace 'COM3' with the name of the serial port on your computer
    list=[]
    # Read data from Arduino
    for i in range (20):
        line = ser.readline().decode('utf-8').strip()
        line=line.split("\t")
        line = [int(x) for x in line]  # Convert the values to integers
        list.append(line)
        
    list=pd.DataFrame(list)
    list.columns=["THUMB","INDEX","MIDDLE","HEART","PINKY","ACCELERATION"]
    list['LETTER']=letter
    print(list)

    list.to_csv(letter+".csv", index=False)