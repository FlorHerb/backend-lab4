from database import BaseBd
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class PasajeroBD(BaseBd):
    __tablename__ = 'pasajeros'
    dni = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)


