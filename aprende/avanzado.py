#desempaquetado 
nombre, edad, ciudad = ("carlos",20,"sayula")
print(nombre)
print(edad)
print(ciudad)

numeros = [1,2,3,4,5]

primero, *medio, ultimo = numeros
print(primero)
print(medio)
print(ultimo)

#resultado 
#primero = 1
#medio = [2,3,4]
#ultimo = 5

#enumerate 

#cuando nesesotas indice y valor 
#======================================

frutas = ["manzana","pera","uva"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

#0 manzana
#1 pera
#2 uva

#zip
nombres = ["carlos","ana","luis"]
edades = [20,25,30]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)



