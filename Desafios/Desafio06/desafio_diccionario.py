# Uso de diccionarios con ejemplos del TPO
# Ejemplo --> Proyectos

#FALTA HACER "modificar_proyecto"

from uuid import uuid4
from datetime import datetime

"""Atributos de Proyecto: uuid, nombre, uuid_equipo(asignado), created_at, end_date, deleted_at"""

lista_dicc_proyectos = [
    {
    'uuid_proyecto': 'b3a13c68-6c83-4e9f-bd84-53e84b7e1c18', 
    'nombre_proyecto': 'Desarrollo Web',
    'uuid_equipo_asignado': 'ad84bd39-22d8-4cb9-b95a-2a6a3d6e1334',
    'created_at': '2024-10-05 12:34:56',
    'end_date': '2025-12-31 23:59:59',
    'deleted_at': None
}
]

def generar_uuid():
    return str(uuid4())
    
# CRUD

def crear_proyecto():
    """Se le pide ingresar los datos del proyecto y devuelve un dicc 'proyecto' """
    uuid_proyecto = generar_uuid()
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    #uuid_equipo_asignado = obtener_equipos() # revisar, que solo traiga el uuid equipo

    nombre_proyecto = input("Ingrese el nombre del proyecto:") # validar campo
    end_date = input("Ingrese fecha de finalización del proyecto (dd-mm-yyyy):") # validar con datetime

    deleted_at = None #valor inicial, despues cuando haya algun delete, se actualizará

    proyecto = {
        "uuid_proyecto": uuid_proyecto,
        "nombre_proyecto": nombre_proyecto,
       # "uuid_equipo_asignado": uuid_equipo_asignado,
        "created_at": created_at,
        "end_date": end_date,
        "deleted_at": deleted_at
    }

    lista_dicc_proyectos.append(proyecto)
    print("Proyecto creado correctamente.")
    return proyecto

def modificar_proyecto(uuid):
    pass

def mostrar_proyectos(lista):
    print()
    print(" Proyectos ".center(70, "-"))
    for indice, proyecto in enumerate(lista, start = 1):
        print()
        print(f"Proyecto {indice}:")
        print(f"  UUID del Proyecto: {proyecto['uuid_proyecto']}")
        print(f"  Nombre del Proyecto: {proyecto['nombre_proyecto']}")
        print(f"  UUID del Equipo Asignado: {proyecto['uuid_equipo_asignado']}")
        print(f"  Fecha de Creación: {proyecto['created_at']}")
        print(f"  Fecha de Finalización: {proyecto['end_date']}")
        print(f"  Fecha de Eliminación: {proyecto['deleted_at'] if proyecto['deleted_at'] else 'No Eliminado'}")
        print()
        print("-" * 70)
    
def eliminar_proyecto(uuid_proyecto_eliminar):
    proyecto_encontrado = None
    for proyecto in lista_dicc_proyectos:
        if proyecto["uuid_proyecto"] == uuid_proyecto_eliminar:
            proyecto_encontrado = proyecto
    
    if proyecto_encontrado:
        nombre_proyecto = proyecto_encontrado["nombre_proyecto"]
        verificacion = input(f"Seguro que quiere eliminar el proyecto {nombre_proyecto} con UUID:{uuid_proyecto_eliminar}?(s/n):")
        if verificacion.lower() == "s":
            lista_dicc_proyectos.remove(proyecto_encontrado)
            print(f"El Proyecto '{nombre_proyecto}' ha sido eliminado")
        else:
            print("Volviendo...")
    else:
        print(f"No se encontró el proyecto")
    pass

def mostrar_menu():
    print(" Menu ".center(70,"-"))
    print("1. Crear Proyecto")
    print("2. Mostrar Proyectos")
    print("3. Modificar Proyecto")
    print("4. Eliminar Proyecto")
    print("5. Salir")
    print("-" * 70)

def menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción:")

        if opcion == '1':
            crear_proyecto()
        elif opcion == '2':
            mostrar_proyectos(lista_dicc_proyectos)
        elif opcion == '3':
            id = input("Ingrese el UUID del proyecto a modificar:")
            modificar_proyecto(id)
        elif opcion == '4':
            id = input("Ingrese el UUID del proyecto a eliminar:")
            eliminar_proyecto(id)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()