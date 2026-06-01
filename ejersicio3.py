cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

promedio = (cal1 + cal2 + cal3) / 3

print("El promedio es:", promedio)

if promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")  
    