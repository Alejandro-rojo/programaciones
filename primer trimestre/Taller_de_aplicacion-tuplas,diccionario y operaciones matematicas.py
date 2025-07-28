#1-calculadora promedio
# notas=[]
# nota1=float(input("agrega tu nota en ingles: "))
# nota2=float(input("agrega tu nota en matematicas: "))
# nota3=float(input("agrega tu nota en biologia: "))
# notas.append(nota1)
# notas.append(nota2)
# notas.append(nota3)
# suma=(notas[0])+(notas[1])+(notas[2])
# promedio=suma/3
# print(f"tus notas son {notas}, y el promedio es {promedio}")

#2-actualiza promedios
# inventario={
#     "uvas":3000,
#     "banano":4000,
#     "pera":5000

# }
# print(inventario)
# porcentaje=int(input("ingresa el porcentaje de aumento de el precios (%): "))
# inventario["uvas"]+=inventario["uvas"]*(porcentaje/100)
# inventario["banano"]+=inventario["banano"]*(porcentaje/100)
# inventario["pera"]+=inventario["pera"]*(porcentaje/100)
# print(inventario)

#3-conversor de temperaturas
# celcius1=float(input("ingresa la temperatura en celucius del lunes: "))
# celcius2=float(input("ingresa la temperatura en celucius del martes: "))
# celcius3=float(input("ingresa la temperatura en celucius del miercoles: "))
# celcius4=float(input("ingresa la temperatura en celucius del jueves: "))
# celcius5=float(input("ingresa la temperatura en celucius del viernes: "))
# celcius_5=(celcius1, celcius2, celcius4, celcius5)
# farenheig1=celcius1*9/5+32
# farenheig2=celcius2*9/5+32
# farenheig3=celcius3*9/5+32
# farenheig4=celcius4*9/5+32
# farenheig5=celcius5*9/5+32
# farenheig=(farenheig1, farenheig2, farenheig3, farenheig4, farenheig5)
# print(f"ingresaste estas temperatura: {celcius_5}, en farenheig serian asi {farenheig}")

#4-edad promedio con listas
# edad1=int(input("ingresa la edad de la primera persona: "))
# edad2=int(input("ingresa la edad de la segunda persona: "))
# edad3=int(input("ingresa la edad de la tercera persona: "))
# edad4=int(input("ingresa la edad de la cuarta persona: "))
# edad5=int(input("ingresa la edad de la quinta persona: "))
# edades=[edad1, edad2, edad3, edad4, edad5]
# promedio=((edades[0])+(edades[1])+(edades[2])+(edades[3])+(edades[4]))/5
# print(f"el promedio de edades es {promedio}, y la mayor y menor edad son respectivamente: {max(edades)} y {min(edades)}")

#5-Diccionario de frutas
# frutas={
#     "banano":300,
#     "tomate":500,
#     "manzana":600

# }
# kilo_banano=float(input("cunatos kilos de banano quires?: "))
# kilo_tomate=float(input("cunatos kilos de tomate quires?: "))
# kilo_manzana=float(input("cunatos kilos de manzana quires?: "))
# pedido1=kilo_banano*frutas["banano"] 
# pedido2=kilo_tomate*frutas["tomate"]
# pedido3=kilo_manzana*frutas["manzana"]
# total=pedido1+pedido2+pedido3
# print(f"pediste {kilo_banano} de banano, {kilo_tomate} de tomate, {kilo_manzana} de manzana y en total debes pagar {total} en total")

#6-suma de elementos en tuplas
# numeros=()
# numeros_modificables=list(numeros)
# num1=int(input("ingresa un numero entero: "))
# num2=int(input("ingresa un numero entero: "))
# num3=int(input("ingresa un numero entero: "))
# num4=int(input("ingresa un numero entero: "))
# num5=int(input("ingresa un numero entero: "))
# numeros_modificables.append(num1)
# numeros_modificables.append(num2)
# numeros_modificables.append(num3)
# numeros_modificables.append(num4)
# numeros_modificables.append(num5)
# numeros=tuple(numeros_modificables)
# suma=numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]
# print(f"la suma de los numeros es {suma}")

#7-inventario con lista de diccionario
# inventario=[]
# producto1={
#     "nombre": str(input("como se llama el producto: ")),
#     "cantidad":int(input("cuantos hay: ")),
#     "precio":int(input("cual es el precio del producto: "))
# }
# inventario.append(producto1)
# producto2={
#     "nombre":str(input("como se llama el segundo producto: ")),
#     "cantidad":int(input("cuantos hay: ")),
#     "precio":int(input("cual es el precio del producto: "))
# }
# inventario.append(producto2)
# producto3={
#     "nombre":str(input("como se llama el tercer producto: ")),
#     "cantidad":int(input("cuantos hay: ")),
#     "precio":int(input("cual es el precio del producto: "))
# }
# inventario.append(producto3)
# print(inventario)

#8-modificar una lista de precios
# precios=[1000,2000,3000,4000,5000]
# print(precios)
# descuento=float(input("cuanto porcentaje de descuento deseas aplicar(%): "))
# precios[0]-=precios[0]*(descuento/100)
# precios[1]-=precios[1]*(descuento/100)
# precios[2]-=precios[2]*(descuento/100)
# precios[3]-=precios[3]*(descuento/100)
# precios[4]-=precios[4]*(descuento/100)
# print(precios)

#9-notas con tuplas
# notas=(float(input("dime tu nota en ingles: ")), float(input("dime tu nota es matematica: ")), float(input("ingresa tu nota en sociales: ")),float(input("dime tu nota en bilogia: ")))
# print(F"tus notas son {notas} y la mas alta y baja son respectivamente: {max(notas)}, {min(notas)}")

#10-diccionario de conversiones
# medidas={
#   "km":1000,
#   "m":1,
#   "cm":0.01
#  }
# kilo=float(input("cuantos kilometros quieres pasar a metros?: "))
# centi=float(input("cuantos centimetros quieres que pase a metros?: "))
# kilometros=kilo*1000
# centimetros=centi*0.01
# print(f"{kilo} kilometros, son {kilometros} metros y {centi} centimetros son {centimetros} metros")

#11-lista de productos mas IVA
# precios=[int(input("ingresa el primer precio: ")), int(input("ingresa el segunfo precio: ")), int(input("ingresa el tercer precio: "))]

# precios[0]+=precios[0]*(0.19)
# precios[1]+=precios[1]*(0.19)
# precios[2]+=precios[2]*(0.19)
# print(F"sumadole el IVA los precios quedad {precios}")

#12-tupla de operaciones matematicas
# num1=int(input("digita un numero entero: "))
# num2=int(input("digita un numero entero nuevamente: "))
# operaciones=(num1+num2, num1-num2, num1*num2, num1/num2)
# print(operaciones)

#13-diccionario de estudiantes
# zeti={
#     "Juan":float(input("cual es la nota de juan: ")),
#     "Javier":float(input("cual es la nota de javier")),
#     "Sergio":float(input("cual es la nota de sergio"))
# }
# promedio=zeti["Juan"]+zeti["Javier"]+zeti["Sergio"]/3
# print(F"el promedio es {promedio} y las notas son {zeti}")

#14-LIsta de salarios
# precios=[int(input("ingresa el primer salario: ")), int(input("ingresa el segundo salario: ")), int(input("ingresa el tercer salario: ")), int(input("ingresa el cuarto salario: ")), int(input("ingresa el quinto salario: "))]
# precios[0]+=precios[0]*(0.1)
# precios[1]+=precios[1]*(0.1)
# precios[2]+=precios[2]*(0.1)
# precios[3]+=precios[3]*(0.1)
# precios[4]+=precios[4]*(0.1)
# print(F"sumadole el 10% los salarios queda {precios}")

#15-diccionario de impuestos
# productos={
#     "monoplazas":3000,
#     "jets":5000,
#     "misisiles":4000
# }
# print(productos)
# impuestos=int(input("cuanto aumento de impuestos quieres aplicas (%): "))
# productos["monoplazas"]+=productos["monoplazas"]*(impuestos/100)
# productos["jets"]+=productos["monoplazas"]*(impuestos/100)
# productos["misisiles"]+=productos["misisiles"]*(impuestos/100)
# print(productos)

#16-analisis de lista de edades
# edades=[int(input("dime la edad 1: ")), int(input("dime la edad 2: ")), int(input("dime la edad 3: ")), int(input("dime la edad 4: ")), int(input("dime la edad 5: "))]
# edades1=tuple(edades)
# edades[0]-=18
# edades[1]-=18
# edades[2]-=18
# edades[3]-=18
# edades[4]-=18
# print(F"estas son las edades que me diste: {edades1} ahora te voy a mostrar otra lista, los que tengan valores negativos son menores de edad, {edades}")

#17-tuplas con conversion de monedas
# dolal=float(input("ingresa un cantidad de dolares: "))
# conversiones=(dolal*3991, dolal*0.85, dolal*143.65)
# print(f"{dolal} dolares a pesos, euros y yenes es respectivamente: {conversiones}")

#18-diccionario de ventas
# ventas={
#     "coca"=int(input("ingresa un cantidad de coca que vendiste: ")),
#     "pepsi"=int(input("ingresa un cantidad de pepsi que vendiste: ")),
#     "cuatro"=int(input("ingresa un cantidad de cuatro que vendiste: "))

# }
# vendidas=ventas["coca"]+ventas["pepsi"]+ventas["cuatro"]
# print(F"vendimos en total {vendidas} unidades")

#19-lista de temperaturas extremas
# temperaturas=[float(input("dime la temperatura 1: ")), float(input("dime la temperatura 2: ")), float(input("dime la temperatura 3: ")), float(input("dime la temperatura 4: ")), float(input("dime la temperatura 5: ")), float(input("dime la temperatura 6: ")), float(input("dime la temperatura 7: ")), float(input("dime la temperatura 8: ")), float(input("dime la temperatura 9: ")), float(input("dime la temperatura 10: "))]
# temperaturas1=tuple(temperaturas)
# temperaturas2=temperaturas.copy
# temperaturas[0]-=30
# temperaturas[1]-=30
# temperaturas[2]-=30
# temperaturas[3]-=30
# temperaturas[4]-=30
# temperaturas[5]-=30
# temperaturas[6]-=30
# temperaturas[7]-=30
# temperaturas[8]-=30
# temperaturas[9]-=30
# print(F"estas son las edades que me diste: {temperaturas1} ahora te voy a mostrar otra lista, los que tengan valores positivos superan los 30 grados y los que no son menores de 30 y los que tengan valos de entre -20 y -30 son valores menores de 10, {temperaturas}")

#20-actualizar precios con metodos de listas
# precios=[10, 20, 30, 40, 50]
# print(precios)
# eliminar=int(input("ingresa el precio que quieres eliminar: "))
# precios.remove(eliminar)
# agregar=float(input("ingresa un precio que quieras agregar: "))
# print(precios)