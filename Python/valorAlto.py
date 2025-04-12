val1 = int(input("Ingresa un numero: "))
val2 = int(input("Ingresa un numero: "))
val3 = int(input("Ingresa un numero: "))

alto = val1

if val2>alto:
    alto = val2

if val3>alto:
    alto = val3

print("El valor mas alto es: ", alto)