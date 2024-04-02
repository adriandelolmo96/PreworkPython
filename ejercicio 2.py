'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta'''

cuenta = float(input("La cuenta es: "))

propina = (cuenta * 15) / 100

print("El total a pagar con la propina es: ", cuenta + propina)