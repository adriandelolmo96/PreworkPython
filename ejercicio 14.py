'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''

articulo = float(input('intoduzca el precio del articulo para aplicar el descuento del 20%: '))

descuento = (articulo * 0.20)

precio_final = articulo - descuento

print('el precio del articulo con el descuento es: ',precio_final )