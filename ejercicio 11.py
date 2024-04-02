'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual'''

from datetime import datetime

def calcular_edad(año_nacimiento):
    año_actual = datetime.now().year
    edad = año_actual - año_nacimiento
    return edad

año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad_actual = calcular_edad(año_nacimiento)
print("Tu edad actual es:", edad_actual, "años")