'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos'''

minutos_totales = int(input('ingrese los minutos que desea convertir a horas: '))

horas = minutos_totales // 60

minutos = minutos_totales % 60

print(minutos_totales, 'son', horas,'y',minutos,'minutos')