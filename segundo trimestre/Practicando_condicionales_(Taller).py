# #1-positivo, negativo , cero
# numero=float(input("ingresa un numero: "))
# if numero<0:
#     print(f"{numero} es negativo")
# elif numero>0:
#     print(f"{numero} es positivo")
# elif numero==0:
#     print(f"{numero} es 0")
# else:
#     print(f"{numero} invalido")

# #2-calcula el mayor
# numero=float(input("ingresa un numero: "))
# numero1=float(input("ingresa otro numero: "))
# if numero<numero1:
#     print(f"{numero1} es mayor que {numero}")
# elif numero>numero1:
#     print(f"{numero} es mayor que {numero1}")
# elif numero1==numero:
#     print("ambos numeros son iguales")
# else:
#     print("sintax error")

# #3-determina si es par o impar
# numero=float(input("ingresa un numero: "))
# if numero%2==0:
#     print(f"{numero} es par")
# else:
#     print("el numero es impar")

# #4-verifica si esta entre 10 y 20
# numero=float(input("ingresa un numero: "))
# if numero<=10 and numero>=20:
#     print(f"{numero} no ESTA ENTRE 10 Y 20")
# else:
#     print("esta entre 10 y 20")

# #5-calcula el mayor entre los 3
# numero=float(input("ingresa un numero: "))
# numero1=float(input("ingresa otro numero: "))
# numero2=float(input("ingresa un ultimo numero: "))
# if numero<numero1 and numero1>numero2:
#     print(f"{numero1} es mayor que todos")
# elif numero>numero1 and numero>numero2:
#     print(f"{numero} es mayor que todos")
# elif numero1==numero and numero==numero2:
#     print("los numeros son iguales")
# elif numero2>numero and numero2>numero1:
#     print(f"{numero2} es mayor que todos")
# else:
#     print("sintax error")

# #6-calcula el precio con descuneto
# gasto=int(input("cuantos pesos colombianoes gastaste?: "))
# if gasto>100:
#     print("tienes un descuento del 10%")
#     descuento=gasto*0.1-gasto
#     print(f"en total debes pagar {descuento}")
# else:
#     print("no tienes descuento")

##7-puede votar?
# edad=int(input("ingresa tu edad: "))
# if edad>=18:
#     print("puedes votar")
# else:
#     print("no puedes votar")

# #8-vip con descuento
# gasto=int(input("cuantos pesos colombianoes gastaste?: "))
# vip=input("eres vip?(SI/NO)")
# if vip=="SI":
#     print("tienes un descuento del 20%")
#     descuento=gasto*0.2-gasto
#     print(f"en total debes pagar {descuento}")
# else:
#     print("no eres vip, no hay descuento")

##9-es multiplo de 3 y 5 al mismo tiempo
# numero=float(input("ingresa un numero: "))
# if numero%3==0 and numero%5==0:
#      print(f"{numero} es multiplo de 3 y 5 al mismo tiempo")
# else:
#      print(f"{numero} no es multiplo de 3 y 5 al mismo tiempo")

#10-es divisible entre los 2?
# numero=float(input("ingresa un numero: "))
# numero1=float(input("ingresa otro numero: "))
# numero2=float(input("ingresa un ultimo numero: "))
# if numero%numero1==0 and numero%numero2==0:
#     print(f"{numero} es divisible por ambos numero")
# elif numero%numero1==0 and numero%numero2!=0:
#     print(f"{numero} divisible solo por {numero1}")
# elif numero1==numero and numero==numero2:
#     print("los numeros son iguales")
# elif numero%numero1!=0 and numero%numero2==0:
#     print(f"{numero} es divisible solo por {numero2}")
# else:
#     print("sintax error")

# #11-es mayor o menor que 10
# numeros=[float(input("ingresa un numero: ")),2,float(input("ingresa un numero: ")),4,float(input("ingresa un numero: "))]
# if numeros[4]>10:
#     print("mayor a 10")
# else:
#     print("menor o igual que 10")

##12-verfica si el goat esta en la lista
# numeros=[3,5,7,9]
# posicion=numeros.index(7)#con index me arroja el 2, la posicion en la que esta el 7 y pues asi lo encuentro
# if numeros[posicion]==7:
#     print("el 7 esta en la lista")
# else:
#     print("el 7 no esta en la lista")

##13-suma de los dos primeros
# numericons=[4,6,2,8]
# suma=numericons[0]+numericons[1]
# if suma>10:
#     print("suma alta")
# else:
#     print("suma baja")

##14-marta es de ultima
# nombre=["Ana","Luis","Pedro","Marta"]
# print(nombre[3])
# if nombre[3]=="Marta":
#     print("nombre correcto")
# else:
#     print("nombre diferente")

##15-cambialo si es azul
# colombia=["rojo","azul","amarillo"]
# if colombia[1]=="azul":
#     colombia[1]="verde"
#     print(colombia)

##16-si el primer valor es menor que el ultimo
# numeros=(5,8,12,20)
# if numeros[0]<numeros[3]:
#     print("orden asendente")
# else:
#     print("orden decendente")

##17-verifica si es mayor que 30
# edades=(25, 32, 28)
# if edades[1]>30:
#     print("edad mayor que 30")
# else:
#     print("edad igual o mayor a 30")

##18-de tupla a lista
# numeros=(1,2,3)
# numero=list(numeros)#asi se pasa de tupla a lista
# if numero[1]==2:
#     numero[1]=10
#     numeros=tuple(numero)#y aqui es lo contrario
# print(numeros)

##19-cordenadas altas
# cords=(4,9)
# if cords[1]>5:
#     print("coordenada alta")
# else:
#     print("coordenada baja")

##20-son iguales las tuplas?
# tupla1=(3,4)
# tupla2=(3,5)
# if tupla1==tupla2:
#     print("Tuplas iguales")
# else:
#     ("tuplas diferentes")

##21-es un adluto?
# info={
#     "nombre":"juan",
#     "edad":17
# }
# if info["edad"]>=18:
#     print("ES UN ADULTO")
# else:
#     print("MENOR DE EDAD")

##22-camobia la edad a 21
# info={
#     "nombre":"Lucia",
#     "edad":20
# }
# if info["edad"]>18:
#     info["edad"]=21
# print(info)

##23-existe bogota?
# carlangas={
#     "nombre":"Carlos"
# }
# if "ciudad" not in carlangas:#pues a ver esto no nos lo han enseñado  pero es una forma sencilla de decir que no esta en la lista ademas que traducido al español es eso
#     carlangas["ciudad"]="bogota"
#     print(carlangas)

##24-el pan tiene precio?
# panaderia={
#     "producto":"pan",
#     "precio":1200
#     }
# if "precio" in panaderia:
#     print(panaderia["precio"])
# else:
#     print("no hay precio")

##25-hay pan?
# tienda={
#     "pan":1200,
#     "leche":2000
#     }
# if "pan" in tienda:
#     print(tienda["pan"])
# else:
#     print("no disponible")