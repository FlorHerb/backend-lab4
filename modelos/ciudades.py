from pydantic import BaseModel
from modelos.paises import Pais   

class CiudadSinId(BaseModel):
    nombre:str
    id_pais= int
    pais:Pais = None
    
    class Config:
        orm_mode = True
    
class Ciudad(CiudadSinId):
    id:int
    
    
    
    