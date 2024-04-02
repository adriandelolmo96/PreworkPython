'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

palabra = input('Escribe una palabra: ')

palabra_minuscula = palabra.lower()

if palabra_minuscula == palabra_minuscula[::-1]:
  print('La palabra ', palabra, 'es un palindromo')
else:
  print('La palabra ', palabra, 'no es un palindromo')