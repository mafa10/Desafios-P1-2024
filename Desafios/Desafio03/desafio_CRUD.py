"""Hacer un CRUD, mi caso va a ser un CRUD de Libros"""

"""Campos del Libro: ID, TITULO, AUTOR, EDITORIAL, AÑO PUBLI, PAGINAS"""

"""La idea sería pedir los datos del libro por teclado, e ir cargando libro a libro, después, mostrarlos por pantalla en una matriz, poder agregar más, modificar los datos de un libro y poder eliminar un libro."""

def agregar_libro(lib):
    """
    Recibe los datos de un libro y valida la entrada con funciones.
    Crea un diccionario y lo agrega a una lista para almacenarlos.
    """
    id = input("Ingrese un Id:")
    titulo = input("Ingrese el Titulo del Libro:").strip().title()
    autor = validar_autor(input("Ingrese el Nombre del Autor del Libro:"))
    editorial = input("Ingrese la Editorial del Libro:").title()
    anio = validar_anio(input("Ingrese el Año de Publicación del Libro:").strip())
    cantPag = validar_cantPag(input("Ingrese la Cantidad de Páginas del Libro:").strip())
    
    # Uso de Diccionario
    libro = {
        'Id' : id,
        'Titulo' : titulo,
        'Autor'  : autor,
        'Editorial' : editorial,
        'Anio' : anio,
        'CantPag' : cantPag
    }

    # lib = Lista de Diccionarios
    lib.append(libro)
    return lib

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
    while p.isdecimal() == False:
        print("La cantidad de páginas ingresada no es válida")
        p = input("Ingrese la Cantidad de Páginas del Libro:").strip()
    return p

def eliminar_libro():
    pass

def modificar_libro():
    pass

def imprimir_libros():
    pass

def menu():
    """
    Esta funciona albergará un diccionario con el formato crud.
    Es decir, aca el cliente podria elegir que hacer si, agregar un libro o elim o mod.
    """
    m ={

    }

    pass
#Programa Principal
"""
aut,ani,pag = agregar_libro()
print(aut)
print(ani)
print(pag)
"""
lista = [["algebra lineal","jorge draxler","santaolalla","2924","345"]]
libros = agregar_libro(lista)
for libro in libros:
    print(f"Título: {libro[0]}, Autor: {libro[1]}, Editorial: {libro[2]}, Año: {libro[3]}, Páginas: {libro[4]}")