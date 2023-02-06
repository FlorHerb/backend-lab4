from database import BaseBd
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class AeropuertoBD(BaseBd):
    __tablename__ = 'aeropuertos'
    codigo= Column(String(4), primary_key=True)
    nombre= Column(String(50), nullable=False)
    id_ciudad = Column(Integer, ForeignKey('ciudades.id'))
    ciudad = relationship('CiudadBD')
    
    #vuelos_origen=relationship('AeropuertoBD', back_populates='origen_aero',cascade="save-update")
    #vuelos_destino=relationship('AeropuertoBD', back_populates='destino_aero',cascade="save-update")
