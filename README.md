for numero in range (1, 20, 3):
    print(numero)

lista_generada = list(range(1, 11, 2))
print(lista_generada)

mi_bool = (11==6+4) or (3!=3)
print(mi_bool)

#Libreria
from random import*

aleatorio = randint(1, 50)
print(aleatorio)

from random import choice

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = choise(colores)
print(colores)

numeros = list(range(5, 50, 5)
shuffle(numeros)
print(numeros)
