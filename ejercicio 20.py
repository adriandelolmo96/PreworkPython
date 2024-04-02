'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''

numeros = input('Escribe la lista de números que quieres que sume aquí: ')

lista_cadenas = numeros.split()

lista_numeros = [int(numero) for numero in lista_cadenas]

suma_numeros = sum(lista_numeros)

print("La suma de los números es:", suma_numeros)

