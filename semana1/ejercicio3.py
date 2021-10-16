import re

def esEmailValido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def esTelefonoValido(tel):
    regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
    result = re.match(regex, tel)
    if result is None:
        return False
    return True

def esDniValido(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    if (len(dni) == 9):
        letraControl = dni[8].upper()
        numdni = dni[:8]
        if ( len(numdni) == len( [n for n in numdni if n in numeros] ) ):
            if letras[int(numdni)%23] == letraControl:
                return True
    return False

class Persona:

    def __init__(self, nombre='', edad=0, dni='', telefono='', email=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self.__telefono = telefono
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @property
    def telefono(self):
        return self.__telefono

    @property
    def email(self):
        return self.__email

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) == 0:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        if edad < 0 or edad > 200:
            raise ValueError("Edad incorrecta")

        self.__edad = edad

    @dni.setter
    def dni(self, dni):
        if not esDniValido(dni):
            raise ValueError("DNI incorrecto")
        self.__dni = dni


    @telefono.setter
    def telefono(self, telefono):
        if not esTelefonoValido(telefono):
            raise ValueError("El teléfono no es válido")
        self.__telefono = telefono

    @email.setter
    def email(self, email):
        if not esEmailValido(email):
            raise ValueError("El email no es válido")
        self.__email = email


    def mostrar(self):
        print(f"Nombre:{self.nombre} Edad:{self.edad} DNI:{self.dni} Tel:{self.telefono} Email:{self.email}")

    def esMayorDeEdad(self):
        return (self.edad>=18)