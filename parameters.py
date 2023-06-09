import pandas as pd

import numpy as np

path = "parameters/"
letters = ["A", "E", "I", "O", "U"]  # Lista de letras
filenames = ["A.csv", "E.csv", "I.csv", "O.csv", "U.csv"]  # Archivos CSV correspondientes a cada letra
headers = ["THUMB", "INDEX", "MIDDLE", "HEART", "PINKY", "X","Y"]
headers_range=["LETTER","AUDIO","THUMB_MIN", "THUMB_MAX","INDEX_MIN", "INDEX_MAX","MIDDLE_MIN", "MIDDLE_MAX","HEART_MIN","HEART_MAX", "PINKY_MIN","PINKY_MAX","X_MIN","X_MAX","Y_MIN","Y_MAX"]

output = pd.DataFrame(columns=headers)

for letter, filename in zip(letters, filenames):
    file_name = path + filename
    letter_data = pd.read_csv(file_name)
    mean_values = letter_data.mean().round(0).astype(float)
    std_values = letter_data.std().round(0).astype(float)

    mean_row = pd.DataFrame([[letter, "mean"] + mean_values.tolist()], columns=["LETTER", "PARAMETER"] + headers)
    std_row = pd.DataFrame([[letter, "std"] + std_values.tolist()], columns=["LETTER", "PARAMETER"] + headers)

    output = output.append(mean_row, ignore_index=True)
    output = output.append(std_row, ignore_index=True)

output.to_csv(path + 'data.csv', index=False)

rango = pd.DataFrame(columns=headers_range)

j=0
l=0
cte=[[[0,0],[0,0],[100,0],[0,0],[0,0],[0,0],[0,0]],#A
[[0,0],[100,0],[0,0],[0,0],[0,0],[0,0],[0,0]],#E
[[-126,0],[0,50],[0,0],[0,0],[0,0],[0,0],[0,0]],#I
[[0,0],[0,0],[0,200],[0,200],[0,200],[0,0],[0,0]],#O
[[0,0],[0,50],[0,0],[0,0],[0,0],[0,0],[0,0]]]#U



while j<9:
    print(j)
    print(l)
    
    k=0
    print(k)
    for col in headers:
        print(col)
        mean=output[col].iloc[j]
        std=output[col].iloc[j+1]
        min = mean-std+(cte[l][k][0])
        max = mean+std+cte[l][k][1]
        rango.loc[l,("LETTER")]=letters[l]
        rango.loc[l,("AUDIO")]=(l+1)
        rango.loc[l,(col+"_MIN")]=min
        rango.loc[l,(col+"_MAX")]=max
        k=k+1
    l=l+1 
    j=j+2
    print(rango)


rango.to_csv(path + 'rango.csv', index=False)













#for i 
 #   for column in headers:






        #mean_value = output[output["PARAMETER"] == "mean"][column].values[0]
       # std_value = output[output["PARAMETER"] == "std"][column].values[0]

        # Calcular los valores modificados (restar y sumar la desviación estándar)
     #   modified_min = mean_value - std_value
    #    modified_max = mean_value + std_value

        # Agregar los valores modificados al nuevo DataFrame
        #range[column + "_MIN"] = modified_min
        #range[column +"_MAX"] = modified_max
# Agregar las columnas "LETTER" y "PARAMETER" al nuevo DataFrame
    #    column_min=column+"_MIN"
    #    column_max=column+"_MAX"
    #range = range[j].append({column_min:modified_min}, ignore_index=True)
    #range = range[j].append({column_max:modified_max}, ignore_index=True)

# Imprimir el DataFrame modificado
#print(rango)
