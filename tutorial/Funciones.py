	#	Definir funciones reutilizables con def.

# Ejemplo
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Ana")
print(mensaje)

	#	Parámetros opcionales y valores por defecto:

def suma(a, b=5):  # b tiene un valor por defecto
    return a + b

print(suma(3))      # Resultado: 8
print(suma(3, 2))   # Resultado: 5