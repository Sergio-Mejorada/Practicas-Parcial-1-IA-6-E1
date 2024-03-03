#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 27
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',  #declaracion de teclado 1
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',       #declaracion teclado 2
	'Precio': '59,99'
}

c1 = teclado2["Modelo"]  #almacenamos la prier consulta
c2 = teclado2["Precio"]  #amacenamos la segunda
print("El modelo ", c1, " cuesta ", c2, "$")

print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')
