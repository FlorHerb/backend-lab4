from database import BaseBd
from sqlalchemy import Column,String,Integer, ForeignKey, DateTime, Float, Date
from sqlalchemy.orm import relationship

class AvionBD(BaseBd):
    __tablename__='aviones'
    codigo = Column(String(3), primary_key=True)
    marca = Column(String(50), nullable= False)
    modelo = Column(String(50), nullable=False)
    capacidad = Column(Integer, nullable=False)