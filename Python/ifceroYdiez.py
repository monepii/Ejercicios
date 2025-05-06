
while True:
    try:
        a = float(input("Ingresa un valor: "))  

        if 0 <= a <= 10:
            print("Tu valor está dentro")
        else:
            print("No está dentro")
        break
    except ValueError:
        print("Tienes que ingresar un numero")
