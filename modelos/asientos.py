from pydantic import BaseModel
from modelos.pasajes import Pasaje

class AsientoSinCod(BaseModel):
    num_asiento:int
    cod_vuelo:str
    id_pasaje:int = None
    
    class Config:
        orm_mode = True
     

    
class Asiento(AsientoSinCod):
    id:int
    pasaje: Pasaje = None
    