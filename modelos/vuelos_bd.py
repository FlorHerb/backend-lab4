from database import BaseBd
from sqlalchemy import Column,String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

class VueloBD(BaseBd):
    __tablename__ = 'vuelos'
    codigo= Column(String(5), primary_key=True)
    fecha = Column(Date, nullable=False)
    hora= Column(Time, nullable=False)
    cod_origen_aero= Column(String(4), ForeignKey('aeropuertos.codigo'))
    cod_destino_aero= Column(String(4), ForeignKey('aeropuertos.codigo'))
    cod_avion = Column(String(3), ForeignKey('aviones.codigo'))
    
    avion= relationship('AvionBD')
    origen_aero= relationship('AeropuertoBD')
    destino_aero=relationship('AeropuertoBD')
    
   