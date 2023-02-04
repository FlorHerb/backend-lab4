from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.aviones import Avion
from repos.aviones_repo import AvionRepo

avion_api = APIRouter(prefix='/aviones', tags=['Aviones'])
avion_repo = AvionRepo()

@avion_api.get('', response_model=list[Avion])
def get_all(db:Session = Depends(get_db)):
    result = avion_repo.get_all(db)
    return result

@avion_api.get('/{id}', response_model=Avion)
def get_by_id(id: str, db:Session = Depends(get_db)):
    result = avion_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Avion no encontrada')
    return result

@avion_api.post('', response_model=Avion, status_code=201)
def nuevo(datos:Avion, db:Session = Depends(get_db)):
    result = avion_repo.agregar(db, datos)
    if result is None:
        raise HTTPException(status_code=400,detail='El largo del código es incorrecto')
    return result


@avion_api.put('/{id}', response_model=Avion)
def modificar(id:str, datos:Avion, db:Session = Depends(get_db)):
    result = avion_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Avion no encontrada')

    return result

@avion_api.delete('/{id}', status_code=204)
def borrar(id:str, db:Session = Depends(get_db)):
    result = avion_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Avion no encontrada')

    return