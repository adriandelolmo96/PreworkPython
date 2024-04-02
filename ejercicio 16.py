'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''

numeros = input('ingrese los números que desea: ').split()

pares = 0
impares = 0

for numero in numeros: 
   numero = int(numero)

   if numero % 2 == 0:
     pares +=1
   else:
      impares +=1