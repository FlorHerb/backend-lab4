from pydantic import BaseModel
from datetime import date, time
from modelos.aviones import Avion
from modelos.aeropuertos import Aeropuerto
from typing import Optional

class VueloSinCod(BaseModel):
    cod_origen_aero: str = None
    cod_destino_aero: str =None
    fecha: date
    hora: time
    cod_avion: str = None

    class Config:
        orm_mode = True
    
class Vuelo(VueloSinCod):
    codigo: str
    
    
class VueloConObj(Vuelo):
    avion: Avion
    origen_aero : Aeropuerto = None
    destino_aero : Aeropuerto = None        