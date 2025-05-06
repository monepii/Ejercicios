import json

agenda = {}

def cargar():
    global agenda
    try:
        with open("archivo.json", "r") as archivo:
            agenda = json.load(archivo)
    except FileNotFoundError:
        agenda = {}  

def guardar():
    with open("archivo.json", "w") as archivo:
        json.dump(agenda, archivo)
    print("Agenda guardada correctamente!")


def agregar():
    name_input = input("Ingresa el nombre: ").strip().lower()
    if name_input in agendaLower:
        print("Esta persona ya existe!")    
    else:
        phone = int(input(f"Ingresa el celular de {name_input.capitalize()}: "))
        agenda[name_input.capitalize()] = phone
        print("Contacto agregado")

def modificar():
    name_input = input("Ingresa el nombre de la persona: ").strip().lower()
    if name_input in agendaLower:
        real_name = agendaLower[name_input]
        new_phone = int(input(f"Ingresa el nuevo número de {real_name}: "))
        agenda[real_name] = new_phone
        print("Contacto actualizado")
    else:
        print("No existe :(")

def buscar():
    name_input = input("Ingresa el nombre de la persona: ").strip().lower()
    if name_input in agendaLower:
        real_name = agendaLower[name_input]
        print(f"Número de {real_name}: {agenda[real_name]}")
    else:
        print("No existe :(")


def eliminar():
    name_input = input("Ingresa el nombre de la persona a eliminar: ").strip().lower()
    if name_input in agendaLower:
        real_name = agendaLower[name_input]
        eliminado = agenda.pop(real_name)
        print(f"Se ha borrado correctamente a: {real_name}!")
    else:
        print("No existe :(")



opc = 0
cargar()

while opc != 6:
    try:
        print("\nAGENDA")
        print("1. Agregar Contacto.")
        print("2. Modificar Contacto.")
        print("3. Buscar Contacto.")
        print("4. Mostrar agenda.")
        print("5. Eliminar Contacto.")
        print("6. Guardar y Cerrar")
        opc = int(input("Escribe un número: "))
    
        agendaLower = {nombre.lower(): nombre for nombre in agenda}

        if opc == 1:
            agregar()
        elif opc == 2:
            modificar()
        elif opc == 3:
            buscar()
        elif opc == 4:
            print("\nAgenda actual:")
            for nombre, numero in agenda.items():
                print(f"{nombre}: {numero}")
        elif opc == 5:
            eliminar()
        elif opc == 6:
            guardar()  
            print("Agenda cerrada")

    except ValueError:
        print("Error: Debes ingresar un número.")
