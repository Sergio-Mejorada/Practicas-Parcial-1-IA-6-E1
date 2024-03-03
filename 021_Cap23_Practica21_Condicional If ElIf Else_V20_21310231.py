#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 21
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

#>	Mayor que
#<	Menor que
#>=	Mayor o igual que
#<=	Menor o igual que
#==	Igual que
#!=	Diferente que

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad >= 45 and edad <= 100:
        print('Eres mayor de edad. ya eres un poco grande')
elif edad >= 100 and edad <= 120:
        print('Eres demasiado mayor')
else:
	print('Edad no válida.')
