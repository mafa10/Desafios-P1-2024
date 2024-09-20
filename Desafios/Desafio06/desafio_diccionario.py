# Uso de diccionarios con ejemplos del TPO
# Ejemplo --> Proyectos

from uuid import uuid4
from datetime import datetime

"""Atributos de Proyecto: uuid, nombre, uuid_equipo(asigando), created_at, end_date, deleted_at"""

lista_dicc_proyectos = []

def generar_uuid():
    return str(uuid4())
    
# CRUD

def crear_proyecto():
    """Se le pide ingresar los datos del proyecto y devuelve un dicc 'proyecto' """
    uuid_proyecto = generar_uuid()
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    uuid_equipo_asignado = obtener_equipos() # revisar, que solo traiga el uuid equipo

    nombre_proyecto = input("Ingrese el nombre del proyecto:") # validar campo
    end_date = input("Ingrese fecha de finalización del proyecto (dd-mm-yyyy):") # validar con datetime

    deleted_at = None #valor inicial, despues cuando haya algun delete, se actualizará

    proyecto = {
        "uuid_proyecto": uuid_proyecto,
        "nombre_proyecto": nombre_proyecto,
        "uuid_equipo_asignado": uuid_equipo_asignado,
        "created_at": created_at,
        "end_date": end_date,
        "deleted_at": deleted_at
    }

    lista_dicc_proyectos.append(proyecto)

    return proyecto

def modificar_proyecto():
    pass

def mostrar_proyectos(lista):
    print()
    print("-"*30,"Proyectos","-"*30)
    for indice, proyecto in enumerate(lista, start = 1):
        print()
        print(f"Proyecto {indice}:")
        print(f"  UUID del Proyecto: {proyecto['uuid_proyecto']}")
        print(f"  Nombre del Proyecto: {proyecto['nombre_proyecto']}")
        print(f"  UUID del Equipo Asignado: {proyecto['uuid_equipo_asignado']}")
        print(f"  Fecha de Creación: {proyecto['created_at']}")
        print(f"  Fecha de Finalización: {proyecto['end_date']}")
        print(f"  Fecha de Eliminación: {proyecto['deleted_at'] if proyecto['deleted_at'] else 'No eliminado'}")
        print("-" * 72)
    

def eliminar_proyecto():
    pass

def obtener_equipos():
    #crear equipos hardcodeados para asiganr a proyectos
    pass

def menu():
    pass

crear_proyecto()
mostrar_proyectos(lista_dicc_proyectos)