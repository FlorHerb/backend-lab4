from database import BaseBd
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class AeropuertoBD(BaseBd):
    __tablename__ = 'aeropuertos'
    codigo= Column(String(4), primary_key=True)
    nombre= Column(String(50), nullable=False)
    id_ciudad = Column(Integer, ForeignKey('ciudades.id'))
    ciudad = relationship('CiudadBD')
    
    #vuelos_origen=relationship('VueloBD', back_populates='origen_aero', cascade="all, delete-orphan")
    #vuelos_destino=relationship('VueloBD', back_populates='destino_aero', cascade="all, delete-orphan")
