num1 = int(input("Ingresa número 1: ")) 
num2 = int(input("Ingresa número 2: ")) 
num3 = int(input("Ingresa número 3: ")) 
if num1 >= num2 and num1 >= num3:
    mayor = num1 
elif num2 >= num1 and num2 >= num3: 
    mayor = num2 
else: 
    mayor = num3 
print(f"El mayor de los tres números es: {mayor}")