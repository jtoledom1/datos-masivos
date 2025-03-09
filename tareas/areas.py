def menu():
    print(f"""
        1 Área Triangulo
        2 Área Círculo
        3 Perímetro rectángulo
        4 Área pentágono
        5 Perímetro cuadrado
        6 Salir
        """)
    try:
        opcion_menu=int(input("Ingresa el número de la opción: "))
        return opcion_menu
    except:
        print("Se esperaba un valor numérico")        
    
def area_triangulo(b,h):
    area=(b*h)/2
    return area

def area_circulo(r):
    area=3.141516*r**r
    return area

def perimetro_rectangulo(Lmay,lmen):
    perimetro = (Lmay*2)+(lmen*2)
    return perimetro

def  area_pentagono(l,apotema):
    perimetro= 5 * l
    area= (perimetro * apotema) / 2
    return area

def perimetro_cuadrado(l):
    perimetro = 4*l
    return perimetro

Condicion_de_entrada = 0

while Condicion_de_entrada != 1:

    try:
        resultado_menu=menu()
        match resultado_menu:
            case 1:
                print("Área Triángulo")
                try:
                    b=int(input("Ingresa la base: "))
                    h=int(input("Ingresa la altura: "))
                except:
                    print("Ingresa numero valido")
                Area=area_triangulo(b,h)
                print(Area)
            case 2:
                print("Área Círculo")
                try:
                    r=int(input("Ingresa el radio: "))
                except:
                    print("Ingresa numero valido")
                Area=area_circulo(r)
                print(Area)
            case 3:
                print("Perímetro rectángulo")
                try:
                    Lmay=int(input("Ingresa lado mayor: "))
                    lmen=int(input("Ingresa lado menor: "))
                except:
                    print("Ingresa numero valido")
                Perimetro=perimetro_rectangulo(Lmay,lmen)
                print(Perimetro)
            case 4:
                print("Área pentágono")
                try:
                    l=int(input("Ingresa lado: "))
                    Apotema=int(input("Ingresa apotema: "))
                except:
                    print("Ingresa numero valido")
                Area=area_pentagono(l,Apotema)
                print(Area)
            case 5:
                print("Perímetro cuadrado")
                try:
                    l=int(input("Ingresa lado: "))
                except:
                    print("Ingresa numero valido")
                Perimetro=perimetro_cuadrado(l)
                print(Perimetro)
            case 6:
                Condicion_de_entrada= 1
            case _:
                print("Ingresa un número entre 1 y 6")
    except:
        print("err 0")
