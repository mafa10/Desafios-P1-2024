#Defino la lista de Libros
#Campos: Id, Titulo, Año, CantPág.
libros = [ 
    [1, "Los Ojos del Perro Siberiano", 2004, 567],
    [2, "El secreto de sus ojos", 2007, 1005],
    [3, "caídos del mapa 1", 1995, 217],
    [4, "harry potter y el misterio del príncipe", 2005, 607],
    [5, "caídos del mapa 2", 1995, 580]
]

#Recortar los titulos a un max de 15 caracteres.
libros_recortados = [[str(id).zfill(4), titulo[:20].title(), anio, pag]for id, titulo, anio, pag in libros]

#Ordenar la lista por año (más viejo) y por mayor cantidad de páginas.
libros_ordenados_anio = sorted(libros_recortados, key=lambda x: (x[2], -x[3]))

#Imprimir los libros con f-strings
print("Libros".center(41, "-"))
print(f"{'ID':^4} {'Título':^20} {'Año':^4} {'Páginas':>10}")
print("-"*41)
for id, titulo, anio, pag in libros_ordenados_anio:
    print(f"{id:<4} {titulo:20} {anio:4} {pag:10}")