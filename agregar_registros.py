from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import locales
from crear_entidades import centrosdeportivos
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo locales
local1 = locales(nombre="La sazon de Maria", direccion="San Bartolo", reservaciones="aceptadas",
        colaboradores=40)
local2 = locales(nombre="Los morochos de San Carlos", direccion="San Carlos", reservaciones="aceptadas",
        colaboradores=20)
local3 = locales(nombre="Los Hornados de la Vecina", direccion="Carcelen", reservaciones="aceptadas",
        colaboradores=35)
local4 = locales(nombre="Parrilladas de Jimmy", direccion="la Rumiñahui", reservaciones="aceptadas",
        colaboradores=25)
# se agrega los objetos de tipo locales a la sesión
# a la espera de un commit
session.add(local1)
session.add(local2)
session.add(local3)
session.add(local4)

# se crea un objetos de tipo centrosdeportivos
centrodeportivo1 = centrosdeportivos(institucion="Fuerza y Vigor", direccioninstitucion="Mitad del Mundo", servicios="futbol",
        deportistas=40)
centrodeportivo2 = centrosdeportivos(institucion="Mentesana en Cuerposano", direccioninstitucion="La Nanegalito", servicios="basquet",
        deportistas=20)
centrodeportivo3 = centrosdeportivos(institucion="Solo Venciendote Venceras", direccioninstitucion="Comite", servicios="gimnacio",
        deportistas=35)
centrodeportivo4 = centrosdeportivos(institucion="Fuerza delta", direccioninstitucion="La Luz", servicios="king boxing",
        deportistas=25)
# se agrega los objetos de tipo centrosdeportivos a la sesión
# a la espera de un commit
session.add(centrodeportivo1)
session.add(centrodeportivo2)
session.add(centrodeportivo3)
session.add(centrodeportivo4)



# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()

