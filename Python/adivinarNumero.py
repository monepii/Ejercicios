import random
num = random.randint(1,100)
print(num)
a = 0
intentos = 0
while a != num:
    try: 
        intentos += 1 
        a = int(input("Ingresa un número entre 1 y 100: "))
        if a == num:
            print("FELICIDADES LO LOGRASTE!")
            print(f"Número de intentos: {intentos}")
        elif a>num:
            print("El número el menor")
        else:
            print("El número es mayor!")
    except ValueError: 
        print("Ingresa un valor valido!")

