"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""

print("\033c")

paises=("México","Canada","EUA")
varios=("Hola",True,33,3.1416)
"""
print(paises)
print(varios)

for i in paises:
  print(i)

print (f"El pais es: {paises[0]}")

for i in range(0,len(paises)):
  print (paises[i])

opc=0
while opc<len(paises):
  print (paises[opc])
  opc+=1
"""
edades=(23,24,18,20,20.23,24,19,24)

#cuantos=edades.count(24)
#print(cuantos)
#Usando Lists
posiciones=[]
edad=int(input("Edad: "))
posicion=0
for i in range(0,len(edades)): 
  if edades[i]==edad:
    print(F"El numero se encontro en {i}")
    posiciones.append(i)
tuple_posiciones=tuple(posiciones)
print(tuple_posiciones)
#Usando Sets
posiciones={""}
posiciones.clear()
edad=int(input("Edad: "))
posicion=0
for i in range(0,len(edades)): 
  if edades[i]==edad:
    print(F"El numero se encontro en {i}")
    posiciones.add(i)
tuple_posiciones=tuple(posiciones)
print(tuple_posiciones)