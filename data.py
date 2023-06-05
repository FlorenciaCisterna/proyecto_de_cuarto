import serial
import pandas as pd
import csv 
path = "parameters/"
letters = ["A", "E", "I", "O", "U"]  # Lista de letras


# Set up the serial port

letter=str(input("ingrese letra: "))
ser = serial.Serial('COM8', 9600)  # Replace 'COM3' with the name of the serial port on your computer
list=[]
file_name = path + letter + ".csv"
letter_data = pd.read_csv(file_name)
# Read data from Arduino

for i in range (50):
    line = ser.readline().decode('utf-8').strip()
    line=line.split("\t")
    line = [float(x) for x in line]  # Convert the values to integers
    list.append(line)
    print(str(i),line)   
new_data = pd.DataFrame(list, columns=["THUMB", "INDEX", "MIDDLE", "HEART", "PINKY", "X","Y"])

# Add a new column 'LETTER' with the specified letter
new_data['LETTER'] = letter

# Concatenate the new data with the existing letter_data DataFrame
new = pd.concat([letter_data, new_data], ignore_index=False)

# Save the updated DataFrame to the CSV file

new.to_csv(path+letter+".csv", index=False)