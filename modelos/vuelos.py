from pydantic import BaseModel
from datetime import date, time
from modelos.aviones import Avion
from modelos.aeropuertos import Aeropuerto

class VueloSinCod(BaseModel):
    cod_origen_aero: str
    cod_destino_aero: str
    fecha: date
    hora: time
    cod_avion: str
    avion: Avion = None
    origen_aero : Aeropuerto = None
    destino_aero : Aeropuerto = None
    
    class Config:
        orm_mode = True
    
class Vuelo(VueloSinCod):
    codigo: str    