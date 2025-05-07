import json

agenda = {}

class Persona:
    def __init__(self, nombre = "", apPaterno = "", apMaterno = "", genero = "", edad = 0, telefono = None):
        self.setNombre(nombre)
        self.setApPaterno(apPaterno)
        self.setApMaterno(apMaterno)
        self.setGenero(genero)
        self.setEdad(edad)
        self.setTelefono(telefono)
    
    # Setters
    def setNombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre.strip()
        else:
            self.__nombre = ""
    
    def setApPaterno(self, apellido):
        if isinstance(apellido, str) and apellido.strip():
            self.__apellidoPaterno = apellido.strip()
        else: 
            self.__apellidoPaterno = ""

    def setApMaterno(self, apellido):
        if isinstance(apellido, str) and apellido.strip():
            self.__apellidoMaterno = apellido.strip()
        else:
            self.__apellidoMaterno = ""
    
    def setGenero(self, genero):
        if genero.lower() in {"masculino", "femenino", "otro"}:
            self.__genero = genero.strip()
        else:
            self.__genero = ""
    
    def setEdad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            self.__edad = 0

    def setTelefono(self, telefono):
        if isinstance(telefono, int) and telefono >= 0:
            self.__telefono = telefono
        else:
            self.__telefono = None

    # Getters
    def getNombre(self):
        return self.__nombre

    def getApellidoPat(self):
        return self.__apellidoPaterno
    
    def getApellidoMat(self):
        return self.__apellidoMaterno
    
    def getGenero(self):
        return self.__genero
    
    def getEdad(self):
        return self.__edad
    
    def getTelefono(self):
        return self.__telefono
    
    def mostrarInformacion(self):
        print(f"Nombre completo: {self.__nombre} {self.__apellidoPaterno} {self.__apellidoMaterno}")
        print(f"Edad: {self.__edad}")
        print(f"Género: {self.__genero}")
        print(f"Teléfono: {self.__telefono}")
        
    def actualizarNombre(self, nuevo):
        if nuevo.strip():
            self.__nombre = nuevo.strip()
            return True 
        return False
            
    def actualizarApPaterno(self, nuevo):
        if nuevo.strip():
            self.__apellidoPaterno = nuevo.strip()
            return True
        return False
    
    def actualizarApMaterno(self, nuevo):
        if nuevo.strip():
            self.__apellidoMaterno = nuevo.strip()
            return True
        return False
    
    def actualizar_genero(self, nuevo_genero):
        if nuevo_genero.lower() in ("masculino", "femenino", "otro"):
            self.__genero = nuevo_genero.capitalize()
            return True
        return False
    
    def actualizarEdad(self, nuevo):
        if isinstance(nuevo, int) and nuevo >=0:
            self.__edad = nuevo
            return True
        return False
    
    def actualizarTelefono(self, nuevo_telefono):
        if isinstance(nuevo_telefono, int) and nuevo_telefono >= 0:
            self.__telefono = nuevo_telefono
            return True
        return False
        

def cargar():
    global agenda
    try:
        with open("archivo.json", "r") as archivo:
            agenda = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        agenda = {} 

def guardar():
    with open("archivo.json", "w") as archivo:
        json.dump(agenda, archivo, indent=4)
    print("Agenda guardada correctamente!")


def agregar():
    name_input = input("Ingresa el nombre: ").strip().lower()
    agendaLower = {nombre.lower(): nombre for nombre in agenda}
    
    if name_input in agendaLower:
        print("Esta persona ya existe!")    
    else:
        apellidoPaterno = input("Apellido Paterno: ")
        apellidoMaterno = input("Apellido Materno: ")
        genero = input("Género: ")
        while genero not in ['masculino', 'femenino']:
            genero = input("Escribe masculino o femenino: ")
        edad = int(input("Edad: "))
        
        telefono = int(input(f"Ingresa el celular de {name_input.capitalize()}: "))
        
        persona = Persona(name_input.capitalize(), apellidoPaterno.capitalize(), apellidoMaterno.capitalize(), genero, edad, telefono)
        agenda[name_input.capitalize()] = {
            'nombre': persona.getNombre(),
            'apellidoPaterno': persona.getApellidoPat(),
            'apellidoMaterno': persona.getApellidoMat(),
            'genero': persona.getGenero(),
            'edad': persona.getEdad(),
            'telefono': persona.getTelefono()
        }
        print("Contacto agregado")

def modificar():
    name_input = input("Ingresa el nombre de la persona: ").strip().lower()
    agendaLower = {nombre.lower(): nombre for nombre in agenda}
    
    if name_input in agendaLower:
        real_name = agendaLower[name_input]
        print(f"Datos actuales de {real_name}:")
        print(f"Nombre: {agenda[real_name]['nombre']} {agenda[real_name]['apellidoPaterno']} {agenda[real_name]['apellidoMaterno']}")
        print(f"Teléfono: {agenda[real_name]['telefono']}")
        print(f"Género: {agenda[real_name]['genero']}")
        print(f"Edad: {agenda[real_name]['edad']}")
        print("")
        new_phone = int(input(f"Ingresa el nuevo número de {real_name}: "))
        agenda[real_name]['telefono'] = new_phone
        print("Contacto actualizado")
    else:
        print("No existe :(")

def buscar():
    name_input = input("Ingresa el nombre de la persona: ").strip().lower()
    agendaLower = {nombre.lower(): nombre for nombre in agenda}
    
    if name_input in agendaLower:
        real_name = agendaLower[name_input]
        print(f"\nDatos de {real_name}:")
        print(f"Nombre completo: {agenda[real_name]['nombre']} {agenda[real_name]['apellidoPaterno']} {agenda[real_name]['apellidoMaterno']}")
        print(f"Teléfono: {agenda[real_name]['telefono']}")
        print(f"Género: {agenda[real_name]['genero']}")
        print(f"Edad: {agenda[real_name]['edad']}")
    else:
        print("No existe :(")


def eliminar():
    name_input = input("Ingresa el nombre de la persona a eliminar: ").strip().lower()
    agendaLower = {nombre.lower(): nombre for nombre in agenda}
    
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
    
        if opc == 1:
            print("")
            agregar()
        elif opc == 2:
            print("")
            modificar()
        elif opc == 3:
            print("")
            buscar()
        elif opc == 4:
            print("")
            print("\nAgenda actual:")
            for nombre, info in agenda.items():
                print(f"{nombre} {info['apellidoPaterno']} {info['apellidoMaterno']}, Teléfono: {info['telefono']}, Edad: {info['edad']}, Género: {info['genero']}")
        elif opc == 5:
            print("")
            eliminar()
        elif opc == 6:
            guardar()  
            print("Agenda cerrada")

    except ValueError:
        print("Error: Debes ingresar un número.")
