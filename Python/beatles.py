# paso 1
beatles = []

# paso 2
print(beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# paso 3
print(beatles)
for i in range(2) :
    a = input("Ingresa el nombre del integrante: ")
    beatles.append(a)
    i += 1

    
# paso 4
print(beatles)
del beatles[3]
del beatles[3]
# paso 5
print("Paso 5:", beatles)
beatles.insert(0, "Ringo Starr")

# probando la longitud de la lista
print("Paso 6:", beatles)
print("Los Fav", len(beatles))


