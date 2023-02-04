from pydantic import BaseModel
from modelos.pasajes import Pasaje

class AsientoSinCod(BaseModel):
    num_asiento:int
    cod_vuelo:str
    id_pasaje:int = 0
    pasaje: Pasaje = None
    
class Asiento(AsientoSinCod):
    id:int
    