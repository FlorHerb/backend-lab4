from database import BaseBd
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

class PasajeBD(BaseBd):
    __tablename__ = 'pasajes'
    id = Column(Integer, primary_key=True)
    cod_vuelo= Column(String(5), ForeignKey('vuelos.codigo'), nullable=False)
    nro_asiento= Column(Integer, nullable=False)
    id_pasajero= Column(Integer, ForeignKey('pasajeros.dni'))
    pasajero= relationship('PasajeroBD')
    asiento = relationship('AsientoBD',back_populates='pasaje',uselist=False)
    vuelo= relationship('VueloBD')
