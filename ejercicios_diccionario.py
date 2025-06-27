auto={
    "marca":"ford",
    "modelo":"mustang",
    "año":2022,
    "placa":34213,
    "cilindraje":40000,
    "apodo":"batimovil"


}
print(auto)
#asi se cambia los valores
auto["año"]=2023
#asi se agregan llaves y valores nuevos
auto["color"]="rojo"
print(auto)
#para quitar valores se usa el "del" y el "pop"
# el del borra la llave y el valor 
del auto["modelo"]
#y el pop borra ambos igual que el "del" pero si llamas al pop te dice la variable
auto.pop("color")
print(auto)
#asi se llama al pop
valor=auto.pop("marca")#esto crea una variable donde se guarda ford
print(valor)#y esto printea la variable que quitamos del diccionario
print(auto)