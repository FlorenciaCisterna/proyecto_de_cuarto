import serial
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_csv():
    seña=input("Ingrese el nombre de la seña a realizar: ")
    # Define the number of data points (50 in your case)
    num_data_points = 50
    # Initialize an empty list to store the data
    full_matrix=[]

    for i in range (3):
        print(i)
        data_matrix = []
        follow=input("Dar comienzo a la seña")
        if follow=="1":
            print("entro")
            ser = serial.Serial('COM8', 9600)  # Read data from Arduino
            while len(data_matrix) < num_data_points:
                    print(len(data_matrix))
                    line=ser.readline()
                    data = line.strip().split(b',')  # Read and decode the line
                    data.pop(0)
                    values = []
                    for val in data:
                        if val.strip():  # Verificar si la cadena no está vacía
                            if val.isdigit():
                                values.append(int(val))
                            else:
                                try:
                                    values.append(float(val))
                                except ValueError:
                                    print(f"No se pudo convertir el valor '{val}' a un número válido.")
                             
                    data_matrix.append(values)  
                    print(line)# Add the list to the data matrix
            print(data_matrix)
            ser.close()
            
            full_matrix.append(data_matrix)
    full_data = pd.DataFrame(full_matrix)
    full_data = full_data.T
    nuevos_nombres = ["T1","T2","T3"]
    full_data.columns = nuevos_nombres
    full_data.to_csv(seña+".csv")



def plot_csv1(name):
    variables = ["THUMB", "INDEX", "MIDDLE", "HEART", "PINKY", "ACCEL_X", "ACCEL_Y", "ACCEL_Z"]
    df = pd.read_csv(name, usecols=["T1", "T2", "T3"])
    var = pd.DataFrame()

    for i in df.columns:
        for h in variables:
            column_name = f"{i}_{h}"
            var[column_name] = df[i].apply(lambda x: float(x.strip('[]').split(',')[variables.index(h)]))
            
    for h in variables:
        if not os.path.exists("plots/"+name[:-4]):
            # Si no existe, crear la carpeta
            os.makedirs("plots/"+name[:-4])
     
        fig, axs = plt.subplots(1, 4, figsize=(15, 5))  # 1 fila y 3 columnas de subplots
        colores = ['r', 'g', 'b']
        # Subplot 1: Variable1 vs Índice
        axs[0].scatter(var.index, var["T1_"+h],c=colores[0])
        axs[0].set_xlabel('Tiempo')
        axs[0].set_ylabel("T1_"+h)

        # Subplot 2: Variable2 vs Índice
        axs[1].scatter(var.index, var["T2_"+h],c=colores[1])
        axs[1].set_xlabel('Tiempo')
        axs[1].set_ylabel("T2_"+h)

        # Subplot 3: Variable3 vs Índice
        axs[2].scatter(var.index, var["T3_"+h],c=colores[2])
        axs[2].set_xlabel('Tiempo')
        axs[2].set_ylabel("T3_"+h)
        
        axs[3].scatter(var.index, var["T1_"+h],c=colores[0])
        axs[3].scatter(var.index, var["T2_"+h],c=colores[1])
        axs[3].scatter(var.index, var["T3_"+h],c=colores[2])
        axs[3].set_xlabel('Tiempo')
        axs[3].set_ylabel('T1,T2,T3')
        
        # Ajustar la disposición de los subplots y mostrar la figura
        plt.tight_layout()
        plt.savefig("plots/"+name[:-4]+"/"+h+'.png')

'''for i in range(6):'''    
#create_csv()
plot_csv1("Mi_Documento.csv")
