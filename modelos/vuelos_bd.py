from database import BaseBd
from sqlalchemy import Column,String, ForeignKey, Date, Time, Table
from sqlalchemy.orm import relationship


class VueloBD(BaseBd):
    __tablename__ = 'vuelos'
    codigo= Column(String(5), primary_key=True)
    fecha = Column(Date, nullable=False)
    hora= Column(Time, nullable=False)
    cod_origen_aero= Column(String(4), ForeignKey('aeropuertos.codigo'))
    cod_destino_aero= Column(String(4), ForeignKey('aeropuertos.codigo'))
    cod_avion = Column(String(3), ForeignKey('aviones.codigo'))
    avion= relationship('AvionBD',back_populates='vuelos')
    origen_aero= relationship('AeropuertoBD',foreign_keys='VueloBD.cod_origen_aero')
    destino_aero=relationship('AeropuertoBD',foreign_keys='VueloBD.cod_destino_aero')
    
    pasajes= relationship('PasajeBD', cascade="all, delete-orphan")
    asientos= relationship('AsientoBD', cascade="all, delete-orphan")
    
    #aeropuertos = relationship('AeropuertoBD', back_populates="vuelos")
    #origen_aero= relationship('AeropuertoBD', primaryjoin="AeropuertoBD.codigo==VueloBD.cod_origen_aero")
    #destino_aero=relationship('AeropuertoBD', primaryjoin="AeropuertoBD.codigo==VueloBD.cod_destino_aero")
    


    
   