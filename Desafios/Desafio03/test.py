def a_l():
    autor = validar_autor(input("Ingrese el Nombre del Autor del Libro:"))
    return autor



def validar_autor(a):
    while a.replace(" ", "").isalpha() == False:
        print("El Nombre del Autor no es válido")
        a = input("Ingrese el Nombre del Autor del Libro:")
    return a

#autor = a_l()
#print(autor)
"""
y = input("Ingrese algo:").strip()
print(y)
"""
id=input("Ingrese un Id:")
if id.isdigit() == False:
    print("el id ingresado no es válido")