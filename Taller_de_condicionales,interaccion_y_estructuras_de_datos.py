# #1-es mayor de edad ,menor de edad o adulto mayor
# edad=int(input("cuantos años tienes?: "))
# if edad<18:
#     print("eres menor de edad")
# elif edad>18 and edad<65:
#     print("eres mayor de edad")
# elif edad>65:
#     print("eres un adulto mayor bro")

##2-es bajo, promedio, alto
# estatura=float(input("cuanto mides (m)?: "))
# if estatura<1.5:
#     print("eres de baja estatura")
# elif estatura>1.5 and estatura<1.8:
#     print("eres de estatura promedio")
# elif estatura>1.8:
#     print("eres alto mi bro, sientete orgulloso")

##3-es multiplo de 2 o 3?
# numero=int(input("ingresa un numero entero: "))
# if numero%3==0 and numero%2==0:
#     print(f"{numero} es multiplo de 2 y de 3 ")
# elif numero%3==0:
#     print(f"{numero} es multiplo de 3")
# elif numero%2==0:
#     print(f"{numero} es multiplo de 2")

##4-determina si el decimal tiene 1,2 o mas decimales
# num = input("Ingresa un número: ")
# if '.' in num:
#     decimal = num.split('.')[1]
#     if len(decimal) == 1:
#         print(f"{num} Tiene 1 decimal")
#     elif len(decimal) > 2:
#         print(f"{num} Tiene más de 2 decimales")
#     else:
#         print(f"{num} Tiene 2 decimales")
# else:
#     print(f"{num} No tiene decimales")

##5-reconoce paises
# paises=("Colombia","Peru","Argentina","Mexico")
# origen=str(input("cual es tu pais de origen?: "))
# if paises[0]==origen:
#     print("eres de colombia parcero")
# elif paises[1]==origen:
#     print("eres de peru causa")
# elif paises[2]==origen:
#     print("eres de argentina che")
# elif paises[3]==origen:
#     print("eres de mexico wey")
# else:
#     print("no conosco tu pais :(")

##6-tipo de sangre
# compatibilidad={
#     "O":"O",
#     "A,B,AB,O":"AB",
#     "O,B":"A",
#     "A,O":"B"

# }
# sangre=str(input("que tipo de sangre eres? (A,B,AB,O): "))
# if sangre==compatibilidad["O"]:
#     print(f"eres compatible solo con O")
# elif sangre==compatibilidad["A,B,AB,O"]:
#     print(f"eres muy bueno, eres conpatible con todos los tipos de sagre")
# elif sangre==compatibilidad["O,B"]:
#     print(f"eres compatible con B o con O")
# elif sangre==compatibilidad["A,O"]:
#     print(f"eres compatible con A o O")

##7-hace frio?
# temperatura=float(input("cuantos grados de temperatura hay?: "))
# if temperatura<10:
#     print("es baja temperatura")
# elif estatura>10 and estatura<25:
#     print("es una temperatura promedio")
# elif estatura>25:
#     print("esta haciendo calor")

##8-calculadora simple
# num1=float(input("ingresa un numero: "))
# num2=float(input("ingresa otro numero: "))
# opcion=int(input("quieres 1.sumar, 2.restar, 3.multiplicar(ingresa 1, 2 o 3)"))
# if opcion==1:
#     suma=num1+num2
#     print(F"{num1} mas {num2} es {suma}")
# elif opcion==2:
#     resta=num1-num2
#     print(F"{num1} menos {num2} es {resta}")
# elif opcion==3:
#     multiplicar=num1*num2
#     print(F"{num1} por {num2} es {multiplicar}")

##9-meses y numeros
# calendario={
#     "enero":1,
#     "febrero":2,
#     "marzo":3,
#      "abril":4,
#     "mayo":5,
#     "junio":6,
#     "julio":7,
#     "agosto":8,
#     "septiembre":9,
#     "octubre":10,
#     "noviembre":11,
#     "diciembre":12

# }
# num=int(input("ingresa un numero del 1 al 12: "))
# if num==calendario["enero"]:
#     print("enero es el mes 1 del año")
# elif num==calendario["febrero"]:
#     print("febrero es el mes 2 del año")
# elif num==calendario["marzo"]:
#     print("marzo es el mes 3 del año")
# elif num==calendario["abril"]:
#     print("abril es el mes 4 del año")
# elif num==calendario["mayo"]:
#     print("mayo es el mes 5 del año")
# elif num==calendario["junio"]:
#     print("junio es el mes 6 del año")
# elif num==calendario["julio"]:
#     print("julio es el mes 7 del año")
# elif num==calendario["agosto"]:
#     print("agosto es el mes 8 del año")
# elif num==calendario["septiembre"]:
#     print("septiembre es el mes 9 del año")
# elif num==calendario["octubre"]:
#     print("octubre es el mes 10 del año")
# elif num==calendario["noviembre"]:
#     print("noviembre es el mes 11 del año")
# elif num==calendario["diciembre"]:
#     print("diciembre es el mes 12 del año")

##10-con que empieza
# numero=input("ingresa un numero de 4 digitos: ")
# if numero[0]=="0":
#     print(f"{numero} empieza por 0")
# elif numero[0]=="1":
#     print(f"{numero} empieza por 1")
# elif numero[0]=="2":
#     print(f"{numero} empieza por 2")
# elif numero[0]=="3":
#     print(f"{numero} empieza por 3")
# elif numero[0]=="4":
#     print(f"{numero} empieza por 4")
# elif numero[0]=="5":
#     print(f"{numero} empieza por 5")
# elif numero[0]=="6":
#     print(f"{numero} empieza por 6")
# elif numero[0]=="7":
#     print(f"{numero} empieza por 7")
# elif numero[0]=="8":
#     print(f"{numero} empieza por 8")
# elif numero[0]=="9":
#     print(f"{numero} empieza por 9")
# elif numero[0]=="10":
#     print(f"{numero} empieza por 10")


# #11-vocales, numeros y consonantes
# palabra=input("ingresa una palabra en minusculas totalmente: ")
# if palabra[0]== "a":
#     print("tu palabra empieza por una vocal")
# elif palabra[0]== "e":
#     print("tu palabra empieza por una vocal")
# elif palabra[0]== "i":
#     print("tu palabra empieza por una vocal")
# elif palabra[0]== "o":
#     print("tu palabra empieza por una vocal")
# elif palabra[0]== "u":
#     print("tu palabra empieza por una vocal")
# elif palabra[0]=="1":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="2":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="0":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="3":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="4":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="5":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="6":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="7":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="8":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="9":
#     print(f"{palabra} no es una palabra por que empieza por un numero")
# elif palabra[0]=="b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "ñ" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or "x" or "y" or "z":
#     print("tu palabra empieza por una consonante")

##12-fruteria
# inventario=["manzana", "pera", "piña"]
# pedido=str(input("que fruta quieres?: "))
# if pedido==inventario[0]:
#     print("la manzana vale 3000000$")
# elif pedido==inventario[1]:
#     print("la manzana vale 6000$")
# elif pedido==inventario[2]:
#     print("la manzana vale 50$")
# else:
#     print(F"{pedido} no esta disponiblre")

##13-notas y reprobados
# nota=float(input("ingresa tu nota(1-5): "))
# if nota<3:
#     print("reprobaste mi compa :(")
# elif nota>3 and nota<4:
#     print("aprobaste mi hermano :)")
# elif nota>4:
#     print("tienes un desempeño exelente")

##14- es divisible entre 4, 6 o no?
# numero=int(input("ingresa un numero entero: "))
# if numero%4==0 and numero%6==0:
#     print(f"{numero} es divisible entre 4 y de 6 ")
# elif numero%4==0:
#     print(f"{numero} es divisible entre 4")
# elif numero%6==0:
#     print(f"{numero} es divisible entre 6")

##15-sistema de autenticacion
# print("el usuario es: SENA y la clave es Catatumbo")
# datos={
#     "usuario":"SENA",
#     "clave":"Catatumbo"
# }
# intentoU=input("ingresa tu usuario: ")
# intentoC=input("ingresa tu contraseña: ")
# if intentoC==datos["clave"] and intentoU==datos["usuario"]:
#     print("acceso consedido, validacion correcta")
# else:
#     print("acceso denegado clave o ususario invalido")

##16-a que grupo de edad pertenece
# edad=int(input("cuantos años tienes?: "))
# if edad>=18 and edad<64:
#     print("eres un adulto ya")
# elif edad<=12:
#     print("eres un niño jajjas")
# elif edad>65:
#     print("eres un adulto mayor bro")
# elif edad>=13 and edad<=17:
#     print("eres un adolencente mi pana")

##17-capitales y segundarias
# capitales=["Bogota", "Caracas", "Moscu", "Lima"]
# ciudad=input("ingresa una ciudad: ")
# if ciudad==capitales[0] or ciudad==capitales[1] or ciudad==capitales[2] or capitales==[3]:
#     print(f"{ciudad} es una ciudad capital")
# else:
#     print(f"{ciudad} es una ciudad secundaria por que no esta en mis datos")

##18-valor de compra y descuento
# compra=input("ingresa el valor de tu compra: ")
# if compra>200000:
#     total=compra-compra*0.15
#     print(f"tienes un 15% de descuento, en total debes pagar: {total}")
# elif compra>=100000 and compra<=200000:
#     total=compra-compra*0.1
#     print(f"tienes un 10% de descuento, en total debes pagar: {total}")
# else:
#     print("no hay descuento")

##19-horario de trabajo
# nombre=input("ingresa tu nombre: ")
# horas=float(input("ingresa el numero de horas que trabajaste: "))
# pago=horas*10000
# if horas>=40:
#     pago+=pago*0.1
#     print(pago)
# else:
#     print(pago)

##20-puntaje en la prueba
# puntaje=input("cuanto puntaje sacaste (0-100): ")
# if puntaje<50:
#     print(f"{puntaje} es insuficiente")
# elif puntaje>=50 and puntaje<80:
#     print(f"{puntaje} es aceptable")
# elif puntaje>80:
#     print("tu puntaje es sobresaliente")
