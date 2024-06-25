
from functools import reduce

# Ejercicio 1: Elevar al cuadrado cada elemento de una lista usando map y lambda
lista1 = [1, 2, 3, 4, 5]
resultado1 = list(map(lambda x: x ** 2, lista1))
print(resultado1)

# Ejercicio 2: Filtrar números pares de una lista usando filter y lambda
lista2 = [10, 11, 12, 13, 14]
resultado2 = list(filter(lambda x: x % 2 == 0, lista2))
print(resultado2)

# Ejercicio 3: Sumar dos listas elemento a elemento usando lambda
lista3_1 = [1, 2, 3]
lista3_2 = [4, 5, 6]
resultado3 = list(map(lambda x, y: x + y, lista3_1, lista3_2))
print(resultado3)

# Ejercicio 4: Multiplicar dos listas elemento a elemento usando zip
lista4_1 = [2, 3, 4]
lista4_2 = [5, 6, 7]
resultado4 = list(map(lambda x, y: x * y, lista4_1, lista4_2))
print(resultado4)

# Ejercicio 5: Unir dos listas de strings usando zip
lista5_1 = ['a', 'b', 'c']
lista5_2 = ['x', 'y', 'z']
resultado5 = list(map(lambda x, y: x + y, lista5_1, lista5_2))
print(resultado5)

# Ejercicio 6: Concatenar dos listas de listas usando lambda
lista6_1 = [[1, 2], [3, 4], [5, 6]]
lista6_2 = [['a', 'b'], ['c', 'd'], ['e', 'f']]
resultado6 = list(map(lambda x, y: x + y, lista6_1, lista6_2))
print(resultado6)

# Ejercicio 7: Sumar todos los elementos de una lista usando reduce y lambda
lista7 = [1, 2, 3, 4, 5]
resultado7 = reduce(lambda x, y: x + y, lista7)
print(resultado7)

# Ejercicio 8: Multiplicar todos los elementos de una lista usando reduce y lambda
lista8 = [2, 3, 4, 5]
resultado8 = reduce(lambda x, y: x * y, lista8)
print(resultado8)

# Ejercicio 9: Encontrar el máximo de una lista usando reduce y lambda
lista9 = [10, 2, 30, 4, 50]
resultado9 = reduce(lambda x, y: x if x > y else y, lista9)
print(resultado9)

# Ejercicio 10: Calcular el promedio de una lista usando reduce y lambda
lista10 = [1, 2, 3, 4, 5]
resultado10 = reduce(lambda x, y: x + y, lista10) / len(lista10)
print(resultado10)

# Ejercicio 11: Filtrar números primos de una lista usando filter y lambda
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lista11 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado11 = list(filter(es_primo, lista11))
print(resultado11)

# Ejercicio 12: Convertir una lista de Celsius a Fahrenheit usando map y lambda
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

lista12 = [0, 10, 20, 30, 40]
resultado12 = list(map(lambda c: celsius_a_fahrenheit(c), lista12))
print(resultado12)

# Ejercicio 13: Convertir una lista de kilómetros a millas usando map y lambda
def km_a_millas(km):
    return km * 0.621371

lista13 = [10, 20, 30, 40, 50]
resultado13 = list(map(lambda km: km_a_millas(km), lista13))
print(resultado13)

# Ejercicio 14: Contar la longitud de cada palabra en una lista de strings usando map y lambda
lista14 = ['hola', 'como', 'estas']
resultado14 = list(map(lambda palabra: len(palabra), lista14))
print(resultado14)

# Ejercicio 15: Revertir cada palabra en una lista de strings usando map y lambda
lista15 = ['abc', 'def', 'ghi']
resultado15 = list(map(lambda palabra: palabra[::-1], lista15))
print(resultado15)

# Ejercicio 16: Eliminar valores None de una lista usando filter y lambda
lista16 = [1, None, 2, None, 3, None, 4]
resultado16 = list(filter(lambda x: x is not None, lista16))
print(resultado16)

# Ejercicio 17: Duplicar los valores de una lista usando map y lambda
lista17 = [1, 2, 3, 4]
resultado17 = list(map(lambda x: x * 2, lista17))
print(resultado17)

# Ejercicio 18: Filtrar sublistas de una lista de listas basado en su longitud usando filter y lambda
lista18 = [[1, 2], [3], [4, 5, 6], [7, 8]]
resultado18 = list(filter(lambda sublista: len(sublista) > 2, lista18))
print(resultado18)

# Ejercicio 19: Concatenar dos listas usando reduce y lambda
lista19_1 = [[1, 2], [3, 4], [5, 6]]
lista19_2 = [['a', 'b'], ['c', 'd'], ['e', 'f']]
resultado19 = reduce(lambda x, y: x + y, lista19_1 + lista19_2)
print(resultado19)

# Ejercicio 20: Sumar los elementos de dos listas usando reduce y lambda
lista20_1 = [1, 2, 3]
lista20_2 = [4, 5, 6]
resultado20 = list(map(lambda x, y: x + y, lista20_1, lista20_2))
print(resultado20)

#Cada uno de los resultados impresos corresponderá a la operación solicitada en cada ejercicio.
