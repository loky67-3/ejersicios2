persona = {
    "nombre":"carlos",
    "edad":20,
    "ciudad":"Sayula"
}

#"nombre": -> clave
#"carlos": -> Valor 

#acceder a un valor 
print(persona["nombre"])
print(persona["edad"])


#usar una variable como clave
clave = "ciudad"
print(persona[clave])


#methodo get() 
#mas seguro porque no da error si la clave no existe 
print(persona.get("nombre"))
#carlos 

print(persona.get("telefono"))
#resultado  None 

#con valores por defecto 
print(persona.get("telefono","no registrado"))
#resultado no registrado


#recorrer claves 
for clave in persona:
    print(clave)

#resultado 
#nombre
#edad
#ciudad


#recorrer valores 
for valor in persona.values():
    print(valor)

#carlos 
#20 
#sayula 

#recorrer claves y valores 
for clave, valor in persona.items():
    print(clave, valor)

#resultado 
#nombre carlos 
#edad 20 
#ciudad sayula 



#diccionario dentro de los diccionarios 
usuario = {
    "nombre":"carlos",
    "diccionario": {
        "ciudad":"sayula",
        "pais":"mexico"
    }
}

#acceder 
print(usuario["diccionario"]["ciudad"])
#resultado 
#saYla


#lista de diccionarios 
usuarios = [
    {"nombre":"carlos","edad":20},
    {"nombre":"ana","edad":20},
    {"nombre":"hernes","edad":20},
    {"nombre":"jacob","edad":20},
    {"nombre":"adrian","edad":20}

]

print(usuarios[0]["nombre"])
for usuario in usuarios:
    print(usuario["nombre"])

#carlos 
#ana
#juan
