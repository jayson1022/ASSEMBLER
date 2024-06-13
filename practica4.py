# -*- coding: utf-8 -*-
"""Copia de practica4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-mJd9vrwAHmNRNgdyD_b2Io1sYbsqOLY
"""

# ejercicio 1

num =  [1,2,3,4,5]
num_multiplicados = [a * 3 for a in num]
print(num_multiplicados)

#ejercicio 2

numeros = [5, 10, 15, 20, 25]
numeros_filtrados = [b for b in numeros if b > 10]
print(numeros_filtrados)

#ejercicio 3
palabras = ["hola", "mundo", "python"]
palabras_mayusculas = [palabra.upper() for palabra in palabras]
print(palabras_mayusculas)

#ejercicio 4

palabras = ["hola", "mundo", "python", "programacion"]
palabras_filtradas = [palabra for palabra in palabras if palabra.startswith('p')]
print(palabras_filtradas)

#ejercicio 5

palabras = ["hola", "mundo", "python"]

longitudes = [len(palabra) for palabra in palabras]
print(longitudes)

#ejercicio 6

palabras = ["hola", "mundo", "python", "hi"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 4]
print(palabras_largas)

#ejercicio 7

celsius = [0, 20, 37, 100]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)

#ejercicio 8

fahrenheit = [32.0, 68.0, 98.6, 212.0]
temperaturas_mayores = [temp for temp in fahrenheit if temp > 50]
print(temperaturas_mayores)

#ejercicio 9

numeros = [1, 2, 3, 4, 5]
numeros_sumados = [num + 5 for num in numeros]
print(numeros_sumados)

#ejercicio 10

palabras = ["hola", "mundo", "python", "vida"]
palabras_con_a = [palabra for palabra in palabras if 'a' in palabra]
print(palabras_con_a)