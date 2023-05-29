import serial
import pandas as pd
import csv 
import time 
path=r"parameters\rango.csv"
rango = pd.read_csv(path)

ser = serial.Serial('COM5', 9600)  # Replace 'COM3' with the name of the serial port on your computer

def traduccion(line,rango):
    for j in range(0,5):
        #if rango.loc[j,"THUMB_MIN"]<line[0]<rango.loc[j,"THUMB_MAX"]:
         #   print("thumb ok")
        #else:
         #   print("thumb issue")
        #if rango.loc[j,"INDEX_MIN"]<line[1]<rango.loc[j,"INDEX_MAX"]:
          #  print("index ok")
        #else:
         #   print("index issue")
        #if rango.loc[j,"MIDDLE_MIN"]<line[2]<rango.loc[j,"MIDDLE_MAX"]:
           # print("middle ok")
        #else:
         #   print("middle issue")    
        #if rango.loc[j,"HEART_MIN"]<line[3]<rango.loc[j,"HEART_MAX"]:
            #print("heart ok")
        #else:
           # print("heart issue")
        #if rango.loc[j,"PINKY_MIN"]<line[4]<rango.loc[j,"PINKY_MAX"]:
            #print("pinky ok")
        #else:
         #   print("pinky issue")
        
        if rango.loc[j,"THUMB_MIN"]<=line[0]<=rango.loc[j,"THUMB_MAX"] and rango.loc[j,"INDEX_MIN"]<=line[1]<=rango.loc[j,"INDEX_MAX"] and rango.loc[j,"MIDDLE_MIN"]<=line[2]<=rango.loc[j,"MIDDLE_MAX"] and rango.loc[j,"HEART_MIN"]<=line[3]<=rango.loc[j,"HEART_MAX"] and rango.loc[j,"PINKY_MIN"]<=line[4]<=rango.loc[j,"PINKY_MAX"]:

            letter=rango.loc[j,"LETTER"]
            audio=rango.loc[j,"AUDIO"]
            print(letter)
            print(audio)
           
            return letter,audio
    print("No classification found")
    return None, None


for i in range (0,15):
    line = ser.readline().decode('utf-8').strip()
    line=line.split("\t")
    line = [int(x) for x in line]  # Convert the values to integers
    
#    line=[]
 #   for i in range(0,5):
  #      n=int(input("ingrese valor: "))
   #     line.append(n)
    print(line)
    letter,audio=traduccion(line,rango)
ser.write(audio.encode())