from pydantic import BaseModel
from modelos.pasajeros import Pasajero
from modelos.vuelos import Vuelo


class PasajeSinCod(BaseModel):  
    cod_vuelo: str
    nro_asiento: int
    id_pasajero: int


    class Config:
        orm_mode = True


class Pasaje(PasajeSinCod):
    id: int
    pasajero: Pasajero = None
    vuelo : Vuelo = None
