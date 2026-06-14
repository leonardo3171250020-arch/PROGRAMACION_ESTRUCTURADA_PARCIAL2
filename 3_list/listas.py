print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
print(numeros)

#lista=""
#for i in numeros:
 #   lista+=f"{i}, "

#print (f"[{lista}]")

#lista=""
#for i in range (0,len(numeros)):
 #   lista+=f"{numeros[i]}, "

#print (f"[{lista}]")

lista=""
i=0
while i<len(numeros):
    lista+=f"{numeros[i]}, "
    i+=1

print (f"[{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1er forma

palabras=["UTD","tercer","cuatrimestre","TI"]

palabra=input("Dame la palabra a buscar: ").strip()
if palabra in palabras:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


#2da FORMA
palabras=["UTD","tercer","cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()
encontro=False
for i in palabras:
    if i==palabra:
        encontro=True

if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


#3er FORMA
salida = "["

for i in range(0, len(numeros)):
    salida += f"{numeros[i]}{"," if i < len(numeros)-1 else ""}"

salida += "]"

print(salida)

salida = "["
i = 0
#4ta FORMA
while (i < len(numeros)):
    salida += f"{numeros[i]}{"," if i < len(numeros)-1 else ""}"
    i += 1

salida += "]"

print(salida)
input("Presione Enter para ir hacia los datos de texto.")

print("\033c")

#Ejemplo 3 Añadir elementos a la lista

lista=["hola","que","tal"]

repeticiones=int(input("Cuantos elementos quieres añadir?: "))
for repeteticiones in range (0,repeticiones):
    lista.append(input("Dame un valor: ").strip())

print(lista)

#Opcion 1
true=True
while true:
    lista.append(input("Dame un valor: ").strip())
    true=input("Ingresa True/False para continuar: ").lower().strip()
    if true=="false":
        true=False

print(lista)

#Opcion 2
true="si"
while true=="si":
    lista.append(input("Dame un valor: ").strip())
    true=input("Ingresa Si/No para continuar: ").lower().strip()

print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
    ["Carlos","6181234567"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"],
       ]

#print(agenda)
for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print (agenda[r][c])

cosas=""
for r in range(0,3):
    for c in range(0,2):
        cosas+=f"{agenda [r] [c]},"
    cosas+="\n"
print(f"{cosas}")
