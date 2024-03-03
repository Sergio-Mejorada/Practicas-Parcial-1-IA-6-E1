#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 28
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())



teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x,y in teclado1.items():
    print(x,"= ",y,".")

for x in teclado1:
	print(x, '=', teclado1[x] + '.')
