import re

def val_email(e):
    """Solo se permiten letras (a-z), números (0-9), puntos (.) y caracteres espciales como '_, %, +, -'."""
    patron = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while not re.match(patron, e):
        print("El email ingresado es inválido. Intente nuevamente.")
        e = input("Ingrese un Email: ")
    print("El email ingresado es válido")

def val_num_tel():
    pass

def val_cod_post():
    pass

def val_fecha():
    pass

#Programa Principal
import re
email = val_email(input("Ingrese un Email: "))
"[a-z]" #El guion define un rango de caracteres
"[0-9]"
