# auto={
#     "marca":"ford",
#     "modelo":"mustang",
#     "año":2022,
#     "placa":34213,
#     "cilindraje":40000,
#     "apodo":"batimovil"


# }
# print(auto)
# #asi se cambia los valores
# auto["año"]=2023
# #asi se agregan llaves y valores nuevos
# auto["color"]="rojo"
# print(auto)
# #para quitar valores se usa el "del" y el "pop"
# # el del borra la llave y el valor 
# del auto["modelo"]
# #y el pop borra ambos igual que el "del" pero si llamas al pop te dice la variable
# auto.pop("color")
# print(auto)
# #asi se llama al pop
# valor=auto.pop("marca")#esto crea una variable donde se guarda ford
# print(valor)#y esto printea la variable que quitamos del diccionario
# print(auto)
# print(auto.keys())

# gastos={
#     input("cual es el nobre de la primera persona?: "):int(input("cuanto gasto la primera persona: ")),
#     input("cual es el nobre de la segunda persona?: "):int(input("cuanto gasto la segunda persona: ")),
#     input("cual es el nobre de la tercera persona?: "):int(input("cuanto gasto la  persona tercera: "))
# }
# print(gastos)
# promedio=gastos[input("cual es el nobre de la primera persona?: ")]+gastos[input("cual es el nobre de la segunda persona?: ")]+gastos[input("cual es el nobre de la tercera persona?: ")]/3
# print(promedio)
dicionario=porentaje=100%100-87%100
print(porentaje)