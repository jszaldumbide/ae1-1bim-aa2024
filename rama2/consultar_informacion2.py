"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import base2

# se obtiene la colección general (base de datos)

db = base2.centrodeportivos
coleccion = db.centrodeportivos

# se usa método find_one con parámetros, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one({'nombre':'Fuerza y Vigor'})
print(data_01)

# se usa método find con parámetros, a partir de la colección
print("Muestra todos los documentos de la base de datos que cumplan con la \
condición")
data_02 = coleccion.find({'deportistas':{"$lt":100}})
for registro in data_02:
    print(registro)
