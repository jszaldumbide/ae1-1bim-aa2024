from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada locales, que hereda
# de Base
class locales(Base):
    __tablename__ = 'locales' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombre = Column(String) # atributo de tipo String
    direccion = Column(String)
    reservaciones = Column(String)
    colaboradores = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.direccion, self.reservaciones,
        self.colaboradores)


# Se crea la una entidad llamada centrosdeportivos, que hereda
# de Base
class centrosdeportivos(Base):
    __tablename__ = 'centrosdeportivos' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    institucion = Column(String) # atributo de tipo String
    direccioninstitucion = Column(String)
    servicios= Column(String)
    deportistas = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.institucion, self.direccioninstitucion, self.servicios,
        self.deportistas)



# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
