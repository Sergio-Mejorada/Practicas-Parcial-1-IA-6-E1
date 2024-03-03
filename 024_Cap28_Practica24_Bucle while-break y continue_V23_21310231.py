#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 24
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())



x = 0

#while se ejecuta hasta menor o igual que 30
while x <= 30:
    x += 1   #Incrementos de 1
    
    if x == 4 or x == 6 or x == 10:
        print('Se salto el valor ', x, ' de x')
        continue
    
    if x == 15:
        print('Se rompio la ejecucion del bucle cuando x valia ', x)
        break

#Imprime los resultados que no se corresponde a ninguno de los if
print(x)
