while True:
    a = input("Ingresa diez valores separados por comas: ")

    lista = a.split(",")

    if len(lista)==10:
        print(lista)
        break
    else:
        print("Debes ingresar 10 valores")