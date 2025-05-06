while True:
    try:
        a = float(input("Ingresa un número: "))
        if  0.00 <= a <=10.00:
            print("Bien!")
        elif 11 <= a <=20:
            print("Masomenos:/")
        elif 21<= a <=30:
            print("Pésimo!")
        else:
            print("Fuera del rango!")
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
