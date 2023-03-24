numeros = [1,2,3,4,5,6,7,8,9,10]

for indice, numero in enumerate(numeros):
    numeros[indice]*=10
    indice+=1
print(numeros)

tupla = (100,"hola",[1,2,3,4],-50)
print(tupla[2:])
print(tupla[2][-1])

#conjuntos 
conjunto = set()
conjunto = {1,2,3,4,5,6}

conjunto.add("agregado")
print(conjunto)

conjunto.add(0)
# agrega y ordena a la vez
'5' in conjunto #pregunta si esta en el conjunto
print(conjunto)

grupo = {1,2,3,1,2,3,}
#elimina los duplicados
print(grupo)
# diccionario 
colores = {'amarillo':'yellow','azul':'blue','verde':'green'}
print(colores)
del(colores['amarillo']) #borrar un dato
print(colores)
edad = {'juan':23,'jose':43,'maria':35}
edad['jose']+=1
print(edad)
print(edad['jose'] + edad['juan'])

for e in edad:
    print(e)

for clave in edad:
    print(edad[clave])

for clave in edad:
    print(clave,edad[clave])
# lo mismo que arriba pero mas correcto
for cl, v in edad.items():
    print(cl,v)
#como forma de matrices
p = {'nombre':'legolas','clase':'arquero','raza':'elfo'}
personajes = []
personajes.append(p)
print(p)
p = {'nombre':'gandolf','clase':'mago','raza':'humano'}
personajes.append(p)
print(personajes)

for p in personajes:
    print(p['nombre'], p['clase'], p['raza'])

#pilas colas listas
pila = [1,2,3,4,5]
pila.append(6)
pila.append(7)
print(pila)
n = pila.pop()    #saca el ultimo (se le asigna a una variable)
print(pila, n)
# cola o deque
from collections import deque
cola = deque()
cola = deque(['hector','juan','miguel'])
print(cola)
cola.append('maria')
cola.append('arnaldo')
print(cola)
cola.popleft() #saca el primero de la izquierda
print(cola)

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}


