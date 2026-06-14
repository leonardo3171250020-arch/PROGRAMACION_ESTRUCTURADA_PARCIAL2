"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")
set1={"Hola","123","123","Mexico","Holanda",123,3.1416}

print(set1)

set1.add("Ganador")

print(set1)

set1.pop()
print(set1)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
emails=[]

resp="si"
while resp=="si":
    emails.append(input("Email: ").lower().strip())
    resp=input("¿Deseas insertar otro email?(Si/No): ").lower().strip()

emails_set=set(emails)
emails=list(emails_set)
print(emails) 

#Solucion 2

emails=[]

resp=True
while resp:
    emails.append(input("Email: ").lower().strip())
    cont=input("¿Deseas insertar otro email?(Si/No): ").lower().strip()
    if cont=="no":
        resp=False
        
emails_set=set(emails)
emails=list(emails_set)
print(emails) 




