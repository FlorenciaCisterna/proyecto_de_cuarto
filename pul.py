path=r"parameters/"
import pandas as pd


letter=["A.csv","E.csv","I.csv","O.csv","U.csv"]
for i in letter:
    path= path+i
    pul = pd.read_csv(path)
    for j in range(len(pul["THUMB"])):
        if i== "A.csv"or i=="E.csv" or i=="U.csv" :
            pul["BUTTON"] == 1
            pul.to_csv(path)
        else:
            pul["BUTTON"] == 0
            pul.to_csv(path)
    







