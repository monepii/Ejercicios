def IVA(a,b):
    return (a * b) + a

while True:
    try: 
        valor  = float(input("Ingresa el valor del producto: "))

        if 1500 <= valor <=2500:
            print("El costo con IVA es: ", IVA(valor,.02))
            break

        elif valor > 2500:
            print("El costo con IVA es: ", IVA(valor, .05))
            break

        elif valor < 1500:
            print("El costo con IVA es: ", IVA(valor, .01))
            break

    except ValueError:
        print("Ingresa un valor valido")
