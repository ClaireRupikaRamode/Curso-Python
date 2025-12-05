'''Escribir un programa que realice la siguiente operación aritmética:
(3+2/2*5)^2'''

num1 = 3
num2 = 2
num3 = 5

print("Operación", (num1 + num2 / 2 * num3) ** 2)

'''Resultados sugerido por el curso'''

###Sugerencia 1
print(((3 + 2) / (2 * 5)) ** 2)

###Sugerencia 2
calculo = ((3 + 2) / (2 * 5)) ** 2

print(calculo)

###Sugerencia 3
calculo = pow(((3 + 2) / (2 * 5)), 2)