texto = input("ingrese el texto que desea analizar: ")
texto_transformado = texto.lower()

letra_1 = (input("ingrese la primera letra para buscarla en el texto: ")).lower()
letra_2 = (input("ingerese la segunda letra para buscarla en el texto: ")).lower() 
letra_3 = (input("ingrese la tercera letra para buscarla en el texto: ")).lower()

lista_de_letras = [letra_1, letra_2, letra_3]

conteo_l1 = (texto_transformado.count(lista_de_letras[0]))
conteo_l2 = (texto_transformado.count(lista_de_letras[1]))
conteo_l3 = (texto_transformado.count(lista_de_letras[2]))

print(f"la letra {letra_1} esta {conteo_l1} veces en el texto")
print(f"la letra {letra_2} esta {conteo_l2} veces en el texto")
print(f"la letra {letra_3} esta {conteo_l3} veces en el texto")

palabras = len(texto_transformado.split()) 
print(f"la cantidad de palabras en mi texto es: {palabras}")

letra_inicial = texto_transformado[0]
letra_final = texto_transformado[-1]

print(f"la primera es '{letra_inicial}', y la ultima letra es '{letra_final}'")

texto_invertido = texto_transformado[::-1]
print(f"el texto invertido queda asi: ({texto_invertido})")

palabra_buscar =  (input("ingrese la palabra que quiere buscar: ")).lower()

lista_palabras = texto_transformado.split() 
if(palabra_buscar): 
    print("la palabra({}) SI esta en la frase".format(palabra_buscar))
else:
    print(f"la palabra({palabra_buscar}) NO esta en la frase")
