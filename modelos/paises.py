from pydantic import BaseModel


class PaisSinId(BaseModel):
    nombre:str

    
    class Config:
        orm_mode = True
        
class Pais(PaisSinId):
    id:int