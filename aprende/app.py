#variables y tipos de datos 

nombre = "carlos" #str 
edad = 25      #int
altura = 1.75   #float 
activo = True  #bool 

#ver tipo 
print(type(nombre))

#conversion de tipos 
edad = int("25")
altura = float("1.75")
texto = str(25)


#operadores aritmeticos 
a = 10 
b = 3 
print(a + b) #suma 
print(a - b) #resta
print(a * b) #multiplicacion
print(a / b) #division
print(a % b) #modulo
print(a ** b) #potencia
print(a // b) #division entera




#comparacion 
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#logicos 
True and False #false
True or False #true
not True #false 


#entrada y salida 
nombre = input("tu nombre: ")
print("hola", nombre)

#fstring

edad = 25 
print(f"tengo {edad} años.")

#condicionales 
nota = 80 

if nota >= 80:
    print("A")
elif nota >= 70:
    print("B")
else:
    print("C")



#BUCLES 
contador = 1 
while contador <= 5:
    print(contador)
    contador = contador + 1


for i in range(1, 6):
    print(i)


for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")


#listas 
frutas = ["manzana","pera","uva"]
print(frutas[0])
frutas.append("sandia")

#eliminar
frutas.remove("pera")

for fruta in frutas:
    print(f"fruta: {fruta}")


#diccionarios 
persona = {
    "nombre":"carlos",
    "edad":25
}


#acceder 
print(persona["nombre"])
print(persona["edad"])


#recorrer 
for clave, valor in persona.items():
    print(f"{clave}:{valor}")



#sets 
numeros = {1,2,3,3,3,3}
print(numeros) #no permite duplicados


#funciones 
#con parametros
def saludar(nombre):
    print(f"hola {nombre}")

saludar("carlos")

#retorno 
def suma(a, b):
    return a + b 

resultado = suma(5, 3)


#Scope 
x = 10 
def mostrar():
    print(x)

mostrar()


def prueba():
    y = 5 


#MANEJO DE ERRORES 
try:
    numero = int(input())
except ValueError:
    print("Debes ingresar un numero")


#13 ARCHIVOs 
#escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola mundo")

#leer en un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

