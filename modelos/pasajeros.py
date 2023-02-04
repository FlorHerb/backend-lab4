from pydantic import BaseModel

class PasajeroSinId(BaseModel):
    nombre: str
    class Config:
        orm_mode = True
        
class Pasajero(PasajeroSinId):
    dni: int