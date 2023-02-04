from database import BaseBd
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class PaisBD(BaseBd):
    __tablename__= 'paises'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
