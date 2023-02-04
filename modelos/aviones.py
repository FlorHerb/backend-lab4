from pydantic import BaseModel

class AvionSinCod(BaseModel):
   marca:str
   modelo: str
   capacidad: int
   
   class Config:
       orm_mode= True 
       
class Avion(AvionSinCod):
    codigo: str