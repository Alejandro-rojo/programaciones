#1
#crea una tupla de 1 al 5
# cuenta=()
# respuestas=list(cuenta)
# num1=int(input("cuanto es cero mas uno?: "))
# num2=int(input("cuanto es uno mas uno?: "))
# num3=int(input("cuanto es dos mas uno?: "))
# num4=int(input("cuanto es tres mas uno?: "))
# num5=int(input("cuanto es cuatro mas uno?: "))
# respuestas.append(num1)
# respuestas.append(num2)
# respuestas.append(num3)
# respuestas.append(num4)
# respuestas.append(num5)
# cuenta=tuple(respuestas)
# print(f"si respondiste bien tus respuestas deben ser del 1 al 5, mira {cuenta}")

#2
#accede al segundo elemento
# cuenta=()
# respuestas=list(cuenta)
# num1=int(input("cuanto es cero mas uno?: "))
# num2=int(input("cuanto es uno mas uno?: "))
# num3=int(input("cuanto es dos mas uno?: "))
# num4=int(input("cuanto es tres mas uno?: "))
# num5=int(input("cuanto es cuatro mas uno?: "))
# respuestas.append(num1)
# respuestas.append(num2)
# respuestas.append(num3)
# respuestas.append(num4)
# respuestas.append(num5)
# cuenta=tuple(respuestas)
# uno=cuenta[1]
# print(f"de las respuestas el unico que es par es {uno}")

#3
#muestra la cantidad de elementos
# cuenta=()
# respuestas=list(cuenta)
# num1=int(input("cuanto es cero mas uno?: "))
# num2=int(input("cuanto es uno mas uno?: "))
# num3=int(input("cuanto es dos mas uno?: "))
# num4=int(input("cuanto es tres mas uno?: "))
# num5=int(input("cuanto es cuatro mas uno?: "))
# respuestas.append(num1)
# respuestas.append(num2)
# respuestas.append(num3)
# respuestas.append(num4)
# respuestas.append(num5)
# cuenta=tuple(respuestas)
# print(f"por cierto tengo {numeros} respuestas")

#4
#posicion del 4
# cuenta=()
# respuestas=list(cuenta)
# num1=int(input("cuanto es cero mas uno?: "))
# num2=int(input("cuanto es uno mas uno?: "))
# num3=int(input("cuanto es dos mas uno?: "))
# num4=int(input("cuanto es tres mas uno?: "))
# num5=int(input("cuanto es cuatro mas uno?: "))
# respuestas.append(num1)
# respuestas.append(num2)
# respuestas.append(num3)
# respuestas.append(num4)
# respuestas.append(num5)
# cuenta=tuple(respuestas)
# posicion=cuenta.index(4)
# print(f"la posicion de el numero par mas grande de la lista es {posicion}")

#5
#cuantas veces aprece el 2
# cuenta=()
# respuestas=list(cuenta)
# num1=int(input("cuanto es cero mas uno?: "))
# num2=int(input("cuanto es uno mas uno?: "))
# num3=int(input("cuanto es dos mas uno?: "))
# num4=int(input("cuanto es tres mas uno?: "))
# num5=int(input("cuanto es cuatro mas uno?: "))
# respuestas.append(num1)
# respuestas.append(num2)
# respuestas.append(num3)
# respuestas.append(num4)
# respuestas.append(num5)
# cuenta=tuple(respuestas)
# veces=cuenta.count(2)
# print(f"el 2 aparece {veces} vez en las respuestas que me diste")

#6
#agrega una cadena de texto, decimal y entero
# cuenta=()
# respuestas=list(cuenta)
# texto=str(input("cual es tu nombre?: "))
# num_decimal=float(input("cuanto es uno dividido 2?: "))
# num_entero=int(input("cuanto es dos mas uno?: "))
# respuestas.append(texto)
# respuestas.append(num_decimal)
# respuestas.append(num_entero)
# cuenta=tuple(respuestas)
# print(cuenta)
 
#7
#crea una tupla que tiene otra tupla
tupla_externa=(1,2,(10,20,30),4)
primer_valor_interno=tupla_externa[2][0]
print(f"el primer valor de la tupla interna es: {primer_valor_interno}")