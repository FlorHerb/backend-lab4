from database import BaseBd
from sqlalchemy import Column,String,Integer, ForeignKey, DateTime, Float, Date
from sqlalchemy.orm import relationship

class AsientoBD(BaseBd):
    __tablename__='asientos'
    id= Column(Integer,primary_key=True)
    num_asiento= Column(Integer, nullable=False)
    cod_vuelo= Column(String(5), ForeignKey('vuelos.codigo'))
    id_pasaje= Column(Integer, ForeignKey('pasajes.id'), default=0)
    pasaje = relationship('PasajeBD',back_populates='asiento',uselist=False)