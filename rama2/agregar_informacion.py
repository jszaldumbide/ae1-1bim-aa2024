"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import base2

# se obtiene la colección general (base de datos)

db = base2.locales
coleccion = db.locales

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Los Morochos de San carlos", "direccion": "San bartolo",
"reservaciones":"aceptadas", "colaboradores": 100}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre": "La sazon de Maria", "direccion": "San Carlos", "reservaciones":"aceptadas",
"colabaradores": 90},
{"nombre": "Parrilladas de Jimmy", "direcccion ": "Comite", "reservaciones":"aceptadas",
"colaboradores": 80}
]


db = base2.centrodeportivos
coleccion = db.centrodeportivos

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_02 = {"institucion": "Fuerza y Vigor", "direccioninstitucion": "Mitad del Mundo",
"servicios":"Futbol", "deportistas": 100}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista2 = [
{"institucion": "Mentesana en Cuerposano", "direccioninstitucion": "La Nanegalito", "servicios":"basquet",
"deportistas": 90},
{"institucion": "Solo Venciedote Venceras", "direcccioninstitucion ": "La Luz", "servicios":"king boxing",
"deportistas": 80}
]
coleccion.insert_many(lista)
coleccion.insert_many(lista2)
