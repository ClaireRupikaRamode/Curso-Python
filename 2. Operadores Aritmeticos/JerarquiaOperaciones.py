num1 = 100
num2 = 50
num3 = 25
num4 = 10

print(num1 + num2 * num3)  # Según la jerarquía de operaciones va la multiplicación primero

'''Si quiero forzar que primero se realice la suma, debo usar paréntesis'''
print()
print((num1 + num2) * num3 - num4)  # Primero suma, luego multiplicación y al final resta
print()

'''Ahora si quiero forzar que la resta se realice antes que la multiplicación, debo usar paréntesis'''
print((num1 + num2) * (num3 - num4))  # Primero suma, luego resta y al final multiplicación
print()

'''Se puede llegar a dar con errores si las operaciones llegan a infinito o si se intenta dividir entre cero'''
print((num1 + num2) * (num3 - num4) / (num1 - num1))  # Aquí se intenta dividir entre cero
