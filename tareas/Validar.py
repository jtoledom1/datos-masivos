try:
    precio=int(input("Ingresa precio: "))
except:
    print("mal")

try:
    nombre=input("Ingresa nombre producto: ")
except:
    print("mal")

if precio >= 10000:
    preciofinal=precio*0.97
    print("El precio es: ")
    print(preciofinal)
else:
    for i in range (10):
        precio+=precio
        print(f"{i} el resultado es precio: {precio}")

