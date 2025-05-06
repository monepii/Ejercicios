agenda = {
    "Emmanuel": "1234",
    "Mone": "5657"
}
agendaLower = {nombre.lower(): numero for nombre, numero in agenda.items()}

a = input("Ingresa el nombre de la persona: ").lower() 

if a in agendaLower:
    print(f"Número de {a}: {agendaLower[a]}")
else:
    print("No existe :(")
