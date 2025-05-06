agenda = {
    "mone": "12345", 
    "kevin": "123"
}

try:
    a = int(input("Agenda de Contactos\nIngresa el número de la opción deseada:\n1. Agregar Contacto\n2. Buscar Contacto\nOpción: "))

    if a == 1:
        nombre = input("Ingresa el nombre del contacto: ").strip()
        numTelefono = input(f"Ingresa el número de teléfono para {nombre}: ").strip()
        if nombre and numTelefono:
            agenda[nombre] = numTelefono
            print(f"Contacto {nombre} agregado correctamente.")
        else:
            print("Nombre o número no puede estar vacío.")
    elif a == 2:
        x = input("Ingresa el nombre del contacto que deseas buscar: ").strip()
        if x in agenda:
            print(f"Número de {x}: {agenda[x]}")
        else:
            print(f"{x} no se encuentra en la agenda.")
    else:
        print("Por favor ingresa una opción válida (1 o 2).")
except ValueError:
    print("Debes ingresar un número válido.")

print("\nAgenda actualizada:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")
