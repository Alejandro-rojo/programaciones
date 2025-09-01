# numero=float(input("ingresa un numero: "))
# while numero>0:
#     print(f"{numero}")
#     numero-=1
# print("termino el conteo")

# numero1=int(input("ingresa numero de la tabla de multiplicar: "))
# i=1
# print(f"inicia la tabla del {numero1}")
# while i<=10:
#     print(f"{numero1} * {i}={numero1*i}")
#     i+=1

# x=0
# while True:
#     x-=1
#     print(x)
#     if x==0:
#         break
#     print("fin del bucle")

# #EJERCICIO 1
# cuenta=0#primero creamos la variable a la cual se le va a sumar los numero ingresados
# while True:#empezamos
#     numero=int(input("ingresa un numero entero: "))
#     cuenta+=numero#a cuenta se le suma el numero ingresado
#     if numero==0:
#         break
# print(f"la suma de los numeros que ingresaste es {cuenta}")

# #EJERCICIO 2
# contraseña=""
# while contraseña!="python123":
#     contraseña=input("ingresa la contraseña: ")
# print("contraseña correcta")

# #EJERCICIO 3
# cuenta=[]
# while True:
#     producto=input("ingresa el producto: ")
#     if producto=="fin":
#         break
#     cuenta.append(producto)
# print(f"en total pediste {cuenta}")

#EJERCICIO 4
# i=0
# numeros=[]
# pares=[]
# impares=[]
# while i<10:
#     i+=1
#     numero1=int(input("ingresa un numero entero: "))
#     numeros.append(numero1)
#     if numero1%2==0:
#         pares.append(numero1)
#     elif numero1%2!=0:
#         impares.append(numero1)
# print(f"de los numeros que ingresaste {numeros}, estos son pares {pares} y estos no {impares}")

#EJERCICIO 5

# i=0
# notas=[]
# while True:
#     i+=1
#     nota=float(input("ingresa la nota de 0 a 5: "))
#     pregunta=input("quieres salir del programa?(si/no): ")
#     notas.append(nota)
#     if pregunta=="si":
#         promedio=sum(notas)/i
#         print(f"las notas que ingresaste {notas}, este es el promedio {promedio}")
#         break

#EJERCICIO 6
# numero1=int(input("ingresa numero de la tabla de multiplicar: "))
# i=1
# print(f"inicia la tabla del {numero1}")
# while i<=10:
#     print(f"{numero1} * {i}={numero1*i}")
#     i+=1

#EJERCICIO 7
# secreto=13
# intento=int(input("intenta adivinar mi numero entero: "))
# while intento!=13:
#     intento=int(input("intenta adivinar mi numero entero: "))
#     if intento!=13:
#         if intento>secreto:
#             print(f"el numero secreto es menor que {intento} ")
#         elif intento<secreto:
#             print(f"el numero secreto es mayor que {intento}")
#     else:
#         print("adivinaste el numero era 13 jasajja, entre mas me usas el codigo mas  me crece")

#EJERCICIO 8
# secreto=("pera","kiwi")
# while True:
#     intento=input("intenta adivinar mi fruta: ")
#     if intento not in secreto:
#         print(f"{intento} no es una de mis furtas")
#     elif intento in secreto:
#         print(f"adivinaste la fruta que bien era una de todas estas {secreto}")

#EJERCICIO 9
# diccinario={
#     "negro":"black",
#     "rojo":"red",
#     "azul":"blue",
#     "amarillo":"yellow",
#     "cafe":"coffe"
# }
# while True:
#     intento=input("ingresa la palabra en español: ")
#     if intento in diccinario:
#         print(f"{intento} en ingles es {diccinario[intento]}")
#     elif intento not in diccinario:
#         print(f"{intento} no esta en el diccionario")

#EJERCICIO 10
# while True:
#     num1=float(input("ingresa un numero: "))
#     num2=float(input("ingresa otro numero: "))
#     print("-1. SUMAR  -2. RESTAR  -3.  MULTIPLICAR  -4. DIVIDIR  -5.SALIR")
#     opcciones=int(input("ingresa el numero de la operacion que quieres hacer: "))
#     if opcciones==1:
#         suma=num1+num2
#         print(f"desidiste sumar {num1} y {num2} y eso da como resultado {suma}")
#     elif opcciones==2:
#         resta=num1-num2
#         print(f"desidiste restar {num1} y {num2} y eso da como resultado {resta}")
#     elif opcciones==3:
#         multi=num1*num2
#         print(f"desidiste multiplicar {num1} y {num2} y eso da como resultado {multi}")
#     elif opcciones==4:
#         divi=num1/num2
#         print(f"desidiste dividir {num1} y {num2} y eso da como resultado {divi}")
#     elif opcciones==5:
#         print("saliste de la calculadora")
#         break

#EJERCICIO 11
# i=0
# nombres={
# "nombres":[],
# "edades":[]
# }
# while True:
#     i+=1
#     nombre=input("ingresa el nombre: ")
#     edad=int(input("ingresa la edad: "))
#     pregunta=input("quieres salir del programa?(si/no): ")
#     nombres["nombres"]=nombre
#     nombres["edades"]=edad
#     if pregunta=="si":
#         datos=i
#         print(f"ingresaste {i} nombres y stos son {nombres}")
#         break

#EJERCICIO 12
# secreto=["Azul","Rojo"]
# while True:
#     intento=input("intenta adivinar mi color: ")
#     if intento in secreto:
#         print(f"{intento} es uno de mis colores mira {secreto}")
#     elif intento not in secreto:
#         print(f" no adivinaste la fruta")

#EJERCICIO 13
# numero1=int(input("ingresa numero para potenciarlo: "))
# i=1
# print(f"inicia la potencia del {numero1}")
# while i<=5:
#     print(f"{numero1} ** {i}={numero1**i}")
#     i+=1

#EJERCICIO 14
# i=0
# cuadrados=[]
# while True:
#     i+=1
#     num=float(input("ingresa un numero: "))
#     cuadrado=num**2
#     cuadrados.append(cuadrado)
#     if i==5:
#         print(f"los cuadrados de los numeros que ingresaste son {cuadrados}")
#         break

#EJERCICIO 15
# i=0
# nom=[]
# nots=[]
# base_datos={
# "nombres":nom, 
# "nota_final":nots
# }
# while True:
#     i+=1
#     nombre=input("ingresa el nombre: ")
#     nota=float(input("ingresa la nota fina: "))
#     pregunta=input("quieres salir del programa?(si/no): ")
#     nom.append(nombre)
#     nots.append(nota)
#     if pregunta=="si":
#         datos=i
#         print(f"ingresaste {i} nombres y notas y estos son {base_datos}")
#         break

