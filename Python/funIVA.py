def IVA(a):
    return (a * .16) + a

valor  = float(input("Ingresa el valor del producto: "))
print("El costo con IVA es: ", IVA(valor))
