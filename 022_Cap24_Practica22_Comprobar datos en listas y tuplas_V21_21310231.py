#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 22
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

colores = ("Rojo", "Azul", "Verde", "Amarillo", "Morado", "Naranja")
entrada = input("Introduce un color:\n ")

if entrada in colores[0]:
    print("El rojo si se puede")
elif entrada in colores[1]:
    print("El azul si se puede")
elif entrada in colores[2]:
    print("El verde si se puede")
elif entrada in colores[3]:
    print("El amarillo si se puede")
elif entrada in colores[4]:
    print("El morado si se puede")
elif entrada in colores[5]:
    print("El naranja si se puede")
else:
    print("El color que pusiste no se puede")
