list=[0,1,4,None,4,None,5]
print(len(list))

longitud_lista = len([elemento for elemento in list if elemento is not None])
print(longitud_lista)