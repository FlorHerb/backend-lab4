from database import BaseBd
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship


class CiudadBD(BaseBd):
    __tablename__= 'ciudades'
    id = Column(Integer, primary_key=True)
    nombre= Column(String(50), nullable=False)
    id_pais= Column(Integer, ForeignKey('paises.id'))
    pais= relationship('PaisBD')
    