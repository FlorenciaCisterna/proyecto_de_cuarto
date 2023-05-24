import pandas as pd

letters = ["A","E","I","O","U"]  # Lista de letras
filenames = ["A.csv","E.csv","I.csv","O.csv","U.csv"]  # Archivos CSV correspondientes a cada letra
headers = ["THUMB", "INDEX", "MIDDLE", "HEART", "PINKY", "ACCELERATION", "LETTER", "PARAMETER"]

output = pd.DataFrame(columns=headers)
i = 0

for file, letter in zip(filenames, letters):
    letter_data = pd.read_csv(file)
    output.loc[i, "LETTER"] = letter
    output.loc[i, "PARAMETER"] = "min"

    # Calcular los valores mínimos de cada columna y almacenarlos en el DataFrame de salida
    for header in headers[:-2]:
        output.loc[i, header] = letter_data[header].min()

    output = output.append(output.iloc[i], ignore_index=True)  # Añadir una nueva fila al DataFrame

    output.loc[(i+1), "PARAMETER"] = "max"

    # Calcular los valores máximos de cada columna y almacenarlos en el DataFrame de salida
    for header in headers[:-2]:
        output.loc[(i+1), header] = letter_data[header].max()
    i=i+2

# Imprimir el DataFrame final
print(output)
