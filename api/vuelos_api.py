from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.vuelos import Vuelo
from repos.vuelos_repo import VueloRepo

vuelo_api = APIRouter(prefix='/vuelos', tags=['vuelos'])
vuelo_repo = VueloRepo()

@vuelo_api.get('', response_model=list[Vuelo])
def get_all(db:Session = Depends(get_db)):
    result = vuelo_repo.get_all(db)
    return result

@vuelo_api.get('/{id}', response_model=Vuelo)
def get_by_id(id: str, db:Session = Depends(get_db)):
    result = vuelo_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Vuelo no encontrado')
    return result

@vuelo_api.post('', response_model=Vuelo, status_code=201)
def nuevo(datos:Vuelo, db:Session = Depends(get_db)):
    result = vuelo_repo.agregar(db, datos)
    return result


@vuelo_api.put('/{id}', response_model=Vuelo)
def modificar(id:str, datos:Vuelo, db:Session = Depends(get_db)):
    result = vuelo_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Vuelo no encontrado')

    return result

@vuelo_api.delete('/{id}', status_code=204)
def borrar(id:str, db:Session = Depends(get_db)):
    result = vuelo_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Vuelo no encontrado')

    return