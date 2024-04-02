'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

peso = input('Escriba su peso en kg aqui: ')

altura = input('escriba su altura en cm aqui: ') 

imc = peso / (altura **2)

if imc >= 30:
 print('su índice de masa corporal es: ', imc, 'tiene usted obesidad')
elif imc in range(25,29.9):
  print('su índice de masa corporal es: ', imc, 'superior al normal')
elif imc in range(18, 24.9):
  print('su índice de masa corporal es: ', imc, 'es normal')
elif imc in range(10,17.9):
  print('su índice de masa corporal es: ',imc, 'esta por debajo de lo normal')
else:
  print('Error, compruebe que a introducido son correctos')
