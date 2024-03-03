#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 29
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

del teclado1  #eliminamos todo el diccionario 1
del teclado2['Categoría'] #eliminamos con metodo 'del'
del teclado2['Precio'] #eliminamos con metodo 'pop'

print(teclado2['Modelo']) #imprimimos lo restante del diccionario con print



#Mostramos lo mismo pero con un ciclo for

for x, y in teclado2.items():
	print(x, ": ", y)
