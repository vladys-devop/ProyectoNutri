from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# CONECTAR A LA BD
engine = create_engine("sqlite:///nutrition.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

# TABLA CLIENTES
class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefono = Column(String(15))
    edad = Column(String(3))
    fecha_registro = Column(DateTime)
    peso_inicial = Column(Float)
    altura = Column(Float)
    alergias = Column(String(100))
    intolerancias = Column(String(100))
    objetivos = Column(String(100))
    dietas_pdf = Column(LargeBinary)

    citas = relationship("Cita", back_populates="cliente")
    dietas = relationship("Dieta", back_populates="cliente")

# TABLA CITAS 

class  Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key= True, autoincrement = True)
    cliente_id = Column(Integer,ForeignKey("clientes.id"))
    fecha = Column(DateTime)
    duracion = Column(Integer)
    notas_sesion = Column(String(500))
    completada = Column(Integer, default = 0)

    cliente = relationship("Cliente", back_populates="citas")
    


# TABLA EVOLUCIÓN 

class Evolucion(Base):
    __tablename__ = "evolucion"

    id = Column(Integer,primary_key= True, autoincrement= True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    fecha = Column(DateTime)
    peso = Column(Float)
    notas = Column(String(500))

# TABLA DIETA
class Dieta(Base):
    __tablename__ = "dieta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))  
    nombre = Column(String(100))
    fecha = Column(DateTime)
    archivo = Column(LargeBinary) 
    
    cliente = relationship("Cliente", back_populates="dietas")


# CREAR LAS TABLAS
Base.metadata.create_all(engine)
print("✅ Base de datos creada correctamente")