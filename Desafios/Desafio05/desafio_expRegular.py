import re

def val_email(e):
    """Solo se permiten letras (a-z), números (0-9), puntos (.) y caracteres espciales como '_, %, +, -'."""
    patron = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while not re.match(patron, e):
        print("El email ingresado es inválido. Intente nuevamente.")
        e = input("Ingrese un Email: ")
    print("El email ingresado es válido.")

def val_num_tel(tel):
    """
    Verificacion RegEx:
    # ^\+?(\d{1,3})?\s?-?(\d{2,4})\s?-?(\d{2,4})\s?-?(\d{2,4})$
    Descripcion Paso A Paso:
    # ^ = indica que va al incio de la cadena
    # \+ = la contrabarra para verificar el '+' y no que sea una "función"
    # ? = puedo aparecer 0 o 1 vez con el patron anterior.
    # \d = digitos entre (0-9)
    # {1,3} = entre 1 a 3 caracteres, para el código de area ingresado.
    # ? = puedo aparecer 0 o 1 vez con el patron anterior.
    # \s = "space" un carácter de espacio en blanco
    # -? = puede aparecer 0 o 1 guion.
    # (\d{2,4}) = de 2 a 4 digitos (0-9).
    # \s?-? = repite lo anterior, espacio y guion posible
    # (\d{2,4})\s?-?(\d{2,4}) = igualito
    # $ = busca solo si termina con el patron anterior
    """
    patron = '^\+?(\d{1,3})?\s?-?(\d{2,4})\s?-?(\d{2,4})\s?-?(\d{2,4})$'
    while not re.match(patron, tel):
        print("No se encontro el número de teléfono.")
        tel = input("Marque nuevamente: ")
    print("Teléfono encontrado.")

def val_cod_post(cod):
    patron = '^([A-Za-z]\d{4}[A-Za-z]{3})' # En Arg.
    while not re.match(patron, cod):
        print("Código postal inválido.")
        cod = input("Reingrese un código postal: ")
    print("Código postal válido.")

def val_fecha(date):
    """Formato DD/MM/AAAA"""
    patron = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{1,4})$'
    while not re.match(patron, date):
        print("Fecha inválida.")
        date = input("Reingrese la fecha (DD/MM/AAAA): ")
    print("Fecha válida.")

def val_user(usr):
    """Validación para un usuario con al menos 3 caracteres y hasta 16."""
    patron = '^[a-zA-Z0-9._-]{3,16}$'
    #el patron permite letras min y mayus, números,puntos y guiones entre 3 y 16 caracteres.
    while not re.match(patron, usr):
        print("Nombre de usuario inválido")
        usr = input("Ingrese un nombre de usuario (entre 3 y 16 caracteres): ")
    print("Nombre de usuario válido.")
    pass

def __main__():
    email = val_email(input("Ingrese un Email: "))
    telefono = val_num_tel(input("Ingrese un número de teléfono a buscar: "))
    codPostal = val_cod_post(input("Ingrese un código postal: "))
    fecha = val_fecha(input("Ingrese una fecha (DD/MM/AAAA): "))
    usuario = val_user(input("Ingrese un nombre de usuario (entre 3 y 16 caracteres): "))
    #help(val_num_tel)

#Programa Principal
#"[a-z]" "[0-9]" El guion define un rango de caracteres
__main__()