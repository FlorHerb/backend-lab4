from database import BaseBd
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class AeropuertoBD(BaseBd):
    __tablename__ = 'aeropuertos'
    codigo= Column(String(4), primary_key=True)
    nombre= Column(String(50), nullable=False)
    id_ciudad = Column(Integer, ForeignKey('ciudades.id'))
    ciudad = relationship('CiudadBD',cascade="all, delete-orphan")