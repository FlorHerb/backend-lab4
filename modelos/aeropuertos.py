from pydantic import BaseModel
from modelos.ciudades import Ciudad

class AeropuertoSinCod(BaseModel):
    codigo: str
    nombre: str
    id_ciudad: int
    class Config:
        orm_mode = True
        
class Aeropuerto(AeropuertoSinCod):
    ciudad: Ciudad = None
