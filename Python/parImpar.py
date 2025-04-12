c0 = int(input("Ingresa un numero: "))
i = 1

while c0 != 1:
    
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
    
    
    else: 
        c0 = 3 * c0 + 1
        print(c0)
    i += 1
    
else:

    print("Numero de intentos:", i)
