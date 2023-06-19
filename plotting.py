import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path=r"parameters\rango.csv"
opath=r"imagenes"
# set width of bar
rango= pd.read_csv(path)
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

# set height of bar

for j in range(0,5):
	min = []
	max = []
	for i in rango.columns[2:-5]:
		if i.endswith("MIN"):
			if rango.loc[j,i]<0:
				min.append(0)
			else:
				min.append(rango.loc[j,i])
		else:
			if rango.loc[j,i]<0:
				max.append(0)
			else:
				max.append(rango.loc[j,i])
	
	letter=rango.loc[j,"LETTER"]
	br1 = np.arange(len(min))
	br2 = [x + barWidth for x in br1]
	plt.bar(br1, min, color ='cyan', width = barWidth, edgecolor ='grey', label ='MIN')
	plt.bar(br2, max, color ='blue', width = barWidth, edgecolor ='grey', label ='MAX')
	plt.ylabel(letter, fontweight ='bold', fontsize = 15)
	plt.xticks([r + barWidth for r in range(len(min))],
			['PULGAR', 'INDICE', 'MEDIO', 'CORAZÓN', 'MEÑIQUE'])
	
	plt.legend()
	plt.savefig(opath+ "/"+letter+".jpg")
	plt.clf()

	
	

		
    
    
