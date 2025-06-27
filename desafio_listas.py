LISTA1=[]
LISTA1.append(100)
LISTA1.append("hola mundo")

LISTA2=[]
LISTA2.append("hola y adios")
LISTA2.append(300)

LISTA3=[]
LISTA3=LISTA1.copy()
LISTA3.remove("hola mundo")

LISTA4=[]
LISTA4=LISTA2.copy()
LISTA4.remove(300)
LISTA4.remove("hola y adios")
 
LISTA5=[]
LISTA5.extend(LISTA4)
LISTA5.extend(LISTA3)
print(LISTA1)
print(LISTA2)
print(LISTA3)
print(LISTA4)
print(LISTA5)