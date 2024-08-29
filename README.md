for numero in range (1, 16, 4):
    print(numero)

lista_generada = list(range(1, 15, 2))
print(lista_generada)

mi_bool = (11==6+3) or (3!=3)
print(mi_bool)

#Libreria
from random import*

aleatorio = randint(1, 40)
print(aleatorio)

from random import choice

colores = ['beige', 'rojo', 'lila', 'dorado']
aleatorio = choice(colores)
print(aleatorio)

numeros = choise(colores)
print(colores)

numeros = list(range(6, 60, 6)
shuffle(numeros)
print(numeros)
