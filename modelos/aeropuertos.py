from pydantic import BaseModel
from modelos.ciudades import Ciudad

class AeropuertoSinCod(BaseModel):
    nombre: str
    id_ciudad: int
    ciudad: Ciudad = None
    class Config:
        orm_mode = True
        
class Aeropuerto(AeropuertoSinCod):
    codigo: str
