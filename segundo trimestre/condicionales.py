#verifica si el numero es positivo, negativo o cero 
numero=float(input("ingresa un numero: "))
if numero<0:
    print(f"{numero} es negativo")
elif numero>0:
    print(f"{numero} es positivo")
else:
    print(f"{numero} es cero")

#verifica el mayor de dos numero ingresados
num1=float(input("ingresa un numero: "))
num2=float(input("ingresa otro  numero: "))
if num1>num2:
    print(F"{num2} es menor que {num1}")
elif num1<num2:
    print(F"{num1} es menor que {num2}")
else:
    print(f"{num1} y {num2} son iguales")