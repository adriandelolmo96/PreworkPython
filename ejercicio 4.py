'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

def contar_vocales(palabra):
  contador_de_vocales = 0 

  for letra in palabra:
    if letra in 'AEIOUaeiou':
      contador_de_vocales +=1
  return contador_de_vocales

palabra =input('escribe una palabra: ')

print('el número de vocales en la palabra', palabra, 'es: ', contar_vocales(palabra))