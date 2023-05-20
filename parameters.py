import csv
import numpy as np
import pandas as pd
letters=["A"]#,"E","I","O","U"]
filenames = "C:\Users\flore\Desktop\A.csv"#,"E.csv","I.csv","O.csv","U.csv"]  #cvs files for each letter
headers=["THUMB","INDEX","MIDDLE","HEART","PINKY","ACCELERATION","LETTER""PARAMETER"]

output = pd.DataFrame(columns=headers)


for files in filenames:
    letter=pd.read_csv(files)
    for letter in letters:
        output["LETTER"]= str(letter)
        for i in (headers-2):
            output[i]=letter[i].min()
            output["PARAMETER"]=str(min)
            
        for i in (headers-2):   
            output[i]=letter[i].max()
            output["PARAMETER"]=str(max)

      
     