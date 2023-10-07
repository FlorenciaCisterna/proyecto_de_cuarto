import serial
import pandas as pd
import time 
import numpy as np
#constantes

path=r"parameters\rango.csv"
rango = pd.read_csv(path,header= 0,engine= 'python')
arduino_port = 'COM5'  # Cambia esto al puerto serial correcto en tu computadora
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
           # if rango.loc[i,"BUTTON"]==line[7]:
            #    test[i].append(rango.loc[i,"LETTER"]) 
    return test

def coincidencias(lista_a,lista_b):
    letra_a= lista_a[0]
    letra_b= lista_b[0]
    
    if letra_a == "I" or letra_b=="I":
        print("reconoce la I")
        if letra_a == "E" or letra_b=="E":
            if line[7]== 0:
                letter="E"
            else: 
                letter="I"
            return letter

    
        elif letra_a == "U" or letra_b=="U":
            print("reconoce la u")
            if rango.loc[4,"PINKY_MIN"]<=line[4]<= rango.loc[4,"PINKY_MAX"]:
                letter = "U"
            else:
                letter= "I"
            
            return(letter)
    elif letra_a == "A" or letra_b=="A":
        if line[7]== 0:
            letter="E"
        else: 
            letter="I"
        return letter

############################################ main ###############################################################
 
while True:
    
    try:
        ser = serial.Serial(arduino_port, baud_rate)
        line = ser.readline()
        data = line.strip().split(b',')
        
        data[0]= data[0].decode('utf-8', errors='ignore').strip()
        
        
        #data.pop(0)
        values = [int(val) if val.isdigit() else float(val) for val in data]
     
        #line = ser.readline().decode('utf-8').strip()
        #line = line.split(",")
        #line = [float(x) for x in values]  # Convert the values to integers
        line = [int(x) for x in values]
        print(line)
        if len(line)>0:
                
            test = traduccion(line,rango)

            #verifica la longitud de la lista
            lista_mas_larga = max(test, key=len)
            longitud_lista_mas_larga = len(lista_mas_larga)
            existe_misma_longitud = False
            print(lista_mas_larga)
            for sublista in test:
                if sublista != lista_mas_larga and len(sublista) == longitud_lista_mas_larga and longitud_lista_mas_larga>=3:
                    existe_misma_longitud = True
                    print(sublista[0])
                    print(lista_mas_larga[0])
                    print(longitud_lista_mas_larga)
                    print("existen listas con la misma longitud")
                    letter= coincidencias(sublista,lista_mas_larga)
                    print(letter)
                    letter = rango.loc[rango["LETTER"] == letter]
                    audio = rango.loc[letter.index[0], "AUDIO"]
                    print(audio)
                    audio=str(audio)
                    ser.write(audio.encode())
                    time.sleep(2)
                    ser.close()

            if existe_misma_longitud == False:
                print("distintas longitudes de lista")
                if longitud_lista_mas_larga >= 3:
                    letter = rango.loc[rango["LETTER"] == lista_mas_larga[0]]
                    audio = rango.loc[letter.index[0], "AUDIO"]
                    print(audio)
                    audio=str(audio)
                    ser.write(audio.encode())
                    time.sleep(2)
                    ser.close()

                else:
                    print("No hay coincidencias, se toma nuevamente la seña")
                    ser.close()
        else:
                
                ser.close()            
    except ValueError as e :
        print("Error: ",e)
        print(data)
        ser.close()
    
    
