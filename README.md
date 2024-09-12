import random

juego = list(range(1, 101))

numero1 = 95
numero2 = 34
numero3 = 27

numeros_escogidos = [numero1, numero2, numero3]

def adivinar_numero():
    for intento in range(3):
        adivinanza = int(input("Adivine un número entre 1 y 101: "))
        if adivinanza in numeros_escogidos:
            print("Correcto, Ha adivinado uno de los números.")
            return
        else:
            print("Incorrecto, Intente de nuevo.")
    print("Luego lo lograra ya que no ha adivinado ninguno de los números.")

adivinar_numero()

