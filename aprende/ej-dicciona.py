#ejersicios diccionari

persona = {
    "nombre":"carlos",
    "edad":20
}

print(persona["nombre"])


auto = {
    "marca":"toyota",
    "modelo":"corolla",
}

print(auto["marca"])


producto = {
    "nombre":"laptop",
    "precio":1000
}

print(producto["precio"])


#agrega una nueva clave 
persona = {
    "nombre":"carlos",
}

print(persona.append("edad",20))


#modifca la edad 
persona["edad"] = 21
print(persona["edad"])



#ejersicio 6 recorre el diccionario 
for clave, valor in persona.items():
    print(clave, valor)


#ejercicio 7 
#obten una clave con .get() 
persona.get("nombre")
#carlos


#diccionario anidado 
usuario = {
    "nombre":"carlos",
    "diccionario": {
        "ciudad":"sayula",
        "pais":"mexico"
    }
}

print(usuario["diccionario"]["ciudad"])



#lista de diccionarios 
usuarios = [
    {"nombre":"carlos","edad":20},
    {"nombre":"ana","edad":20},
    {"nombre":"hernes","edad":20},
]

print(usuarios[0]["nombre"])



#calcula la suma de los valores 
notas = {
    "matematicas":90,
    "ingles":80,
    "python":100
}

#pista sum(notas.values())
print(sum(notas.values()))


#encuentra la edad de ana 
usuario = [
    {"nombre":"carlos","edad":20},
    {"nombre":"ana","edad":25},
    {"nombre":"hernes","edad":30},
]

print(usuario[1]["edad"])

#cuantas claves tiene el diccionario 
persona = {
    "nombre":"carlos",
    "edad":20,
    "ciudad":"sayula"
}

print(len(persona))


#eliminar una clave 
persona = {
    "nombre":"carlos",
    "edad":20
}

print(persona.remove("edad"))



#ejercicio 15 
#dado 
ventas = {
    "lunes":100,
    "martes":150,
    "miercoles":200,
    "jueves":180,
    "viernes":300
}

#encuentra 
#total vendido 
#dia con mayor venta 
#promedio de ventas 
print(f"ventas[lunes] + ventas[martes] + ventas[miercoles] + ventas[jueves] + ventas[viernes]")
#total vendido: 930
print(max(ventas, key=ventas.get))
#dia con mayor venta: viernes
print(sum(ventas.values()) / len(ventas))
#promedio de ventas: 186





#diccionario
ventas = {
    "lunes":100,
    "martes":150,
    "miercoles":200,
    "jueves":180,
    "viernes":300
}

#pyhton guarda pares de: 
#clave:           valor
#lunes             100
#martes            150
#miercoles         200
#jueves             180
#viernes            300

#la clave (key) es "lunes", "martes", "miercoles", "jueves", "viernes"
#el valor (value) es "100", "150", "200", "180", "300"

#palabra -> significado 
#clave   ->  valor 


#que hace .values() 
#le dice a python  
#dame soloamente los valores 
#resultado 


dict_values(['100, 150, 200, 180, 300'])
#visualmente 
#lues     100
#martes   150
#miercoles 200
#jueves    180
#viernes   300





#asi que .values() solo te da los valores() 
#100
#150
#200
#180
#300 


#sum significa 
#suma todos los numeros 
numeros = [10, 20, 30]
print(sum(numeros))
#python hace
#10 + 20 + 30
#60 

#en mi codigo 
#sum(ventas.values)

#python ve 
sum([100, 150, 200, 180, 300])
#python hace
#300 + 150 + 200 + 180 + 300
#930

#por eso 
total = sum(ventas.values())
#guarda 
total = 930

#que hace len() 
#longitud o cantidad de elementos 
frutas = ["manzanas","pera","uva"]
print(len(frutas))
#3
#formula matematica 
promedio = suma total / cantidad 
#tus datos 
#100
#150 
#200
#180 
#300 

promedio = total / len(ventas)
#186

#ahora vamos con .get() 
persona = {
    "nombre":"carlos",
    "edad":20
}

persona["nombre"]
#carlos 
#otra forma 
persona.get("nombre")
#carlos


#la diferencia aparece cuando la clave no existe 
#esto 
persona["telefono"]
#keyError
#porque no existe telefono
#pero 
peresona.get("telefono")   #DEVUELVE ERROR POR ESO .GET ES MAS SEGURO 



# que es max max() 
#dame el valor mas grande 
#ejemplo 
numeros = [94,3,6,2,999]
print(max(numeros))
#resultado = 999


#ahora viene la parte dificil 
max(ventas, key=ventas.get)


#si escribes
for dia in ventas:
    print(dia)

#lunes
#martes
#miercoles
#jueves
#viernes

max(ventas)
#no busca la venta mas alta busca la clave mas grande alfabeticamente 
#eso no nos sirve 
#por eso usamos 

#key=ventas.get
#para comparar las claves, usa los valores asociados a ellas.
#python hace algo parecido a esto 
ventas.get("Lunes")
#100
#ventas.get("martes")
150 
