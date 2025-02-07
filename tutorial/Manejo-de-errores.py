	#	Usar try-except para manejar errores.

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: División entre cero")
