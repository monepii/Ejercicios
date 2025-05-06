agenda = {
    "Emmanuel": 1234,
    "Mone": 5657
}

opc = 0

while opc != 5:
    try:
        print("\nAGENDA")
        print("1. Agregar Contacto.")
        print("2. Modificar Contacto.")
        print("3. Buscar Contacto.")
        print("4. Mostrar agenda.")
        print("5. Cerrar")
        opc = int(input("Escribe un número: "))
    
        agendaLower = {nombre.lower(): nombre for nombre in agenda}

        if opc == 1:
            name_input = input("Ingresa el nombre: ").strip().lower()
            if name_input in agendaLower:
                print("Esta persona ya existe!")
            else:
                phone = int(input(f"Ingresa el celular de {name_input.capitalize()}: "))
                agenda[name_input.capitalize()] = phone
                print("Contacto agregado")

        elif opc == 2:
            name_input = input("Ingresa el nombre de la persona: ").strip().lower()
            if name_input in agendaLower:
                real_name = agendaLower[name_input]
                new_phone = int(input(f"Ingresa el nuevo número de {real_name}: "))
                agenda[real_name] = new_phone
                print("Contacto actualizado")
            else:
                print("No existe :(")

        elif opc == 3:
            name_input = input("Ingresa el nombre de la persona: ").strip().lower()
            if name_input in agendaLower:
                real_name = agendaLower[name_input]
                print(f"Número de {real_name}: {agenda[real_name]}")
            else:
                print("No existe :(")

        elif opc == 4:
            print(agenda)
        
        elif opc ==5:
            print("Agenda cerrada")
    except ValueError:
        print("Error: Debes ingresa un numero")    
