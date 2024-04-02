'''Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''

oracion = input('escribe la oración aquí: ').split()

numero_de_palabras = len(oracion)

print('el número de palabras en la oración es: ', numero_de_palabras)