"""Hacer un CRUD, mi caso va a ser un CRUD de Libros"""

"""Campos del Libro: ID, TITULO, AUTOR, EDITORIAL, AÑO PUBLI, PAGINAS"""

"""La idea sería pedir los datos del libro por teclado, e ir cargando libro a libro, después, mostrarlos por pantalla en una matriz, poder agregar más, modificar los datos de un libro y poder eliminar un libro."""

def agregar_libro():
    #Pensar mejor la validacion de los campos.
    #Hacer una funcion aparte para validar cada campo.
    titulo = input("Ingrese el Titulo del Libro:").strip().title()
    autor = validar_autor(input("Ingrese el Nombre del Autor del Libro:"))
    editorial = input("Ingrese la Editorial del Libro:").title()
    anio = validar_anio(input("Ingrese el Año de Publicación del Libro:").strip())
    cantPag = input("Ingrese la Cantidad de Páginas del Libro:")

    return autor.title().strip(), anio

def validar_autor(a):
    while a.replace(" ", "").isalpha() == False:
        print("El Nombre del Autor no es válido")
        a = input("Ingrese el Nombre del Autor del Libro:")
    return a

def validar_anio(y):
    while y.isdecimal() == False:
        print("El Año ingresado no es válido")
        y = input("Ingrese el Año de Publicación del Libro:").strip()
    return y

def validar_cantPag(p):
    pass

def eliminar_libro():
    pass

def modificar_libro():
    pass

def imprimir_libros():
    pass

#Programa Principal

aut,ani = agregar_libro()
print(aut)
print(ani)
