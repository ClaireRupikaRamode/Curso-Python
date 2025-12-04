'''Recordar/anotar las palabras reservadas para evitar errores al programar.'''

print = 64

print(print)  # Esto causará un error porque 'print' es una palabra reservada.

import keyword #Esta biblioteca permite ver cuales son las palabras reservadas en Python

print(keyword.kwlist)  # Muestra la lista de palabras reservadas en Python

'''Ninguna variable puede comenzar con un número o contener espacios.'''

64Mario = 64  # Esto causará un error porque las variables no pueden comenzar con un número.

print(64Mario)

mi variable = 10  # Esto causará un error porque las variables no pueden contener espacios.

print(mi variable)

'''Tampoco se pueden usar caracteres especiales en los nombres de las variables, excepto el guion bajo (_).'''

mi@variable = 10  # Esto causará un error porque las variables no pueden contener caracteres especiales.

print(mi@variable)

'''Siempre colocar variables descriptivas para facilitar la lectura del código y poder darle soporte a largo plazo.'''

n = 10  # Variable poco descriptiva

edad_usuario = 25  # Variable descriptiva

edad_jovenes = 18  # Variable descriptiva