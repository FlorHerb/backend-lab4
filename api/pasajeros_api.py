from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.pasajeros import Pasajero, PasajeroSinId
from repos.pasajeros_repo import PasajeroRepo

pasajero_api = APIRouter(prefix='/pasajeros', tags=['pasajeros'])
pasajero_repo = PasajeroRepo()

@pasajero_api.get('', response_model=list[Pasajero])
def get_all(db:Session = Depends(get_db)):
    result = pasajero_repo.get_all(db)
    return result

@pasajero_api.get('/{id}', response_model=Pasajero)
def get_by_id(id: int, db:Session = Depends(get_db)):
    result = pasajero_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pasajero no encontrado')
    return result

@pasajero_api.post('', response_model=Pasajero, status_code=201)
def nuevo(datos:Pasajero, db:Session = Depends(get_db)):
    result = pasajero_repo.agregar(db, datos)
    return result


@pasajero_api.put('/{id}', response_model=Pasajero)
def modificar(id:int, datos:PasajeroSinId, db:Session = Depends(get_db)):
    result = pasajero_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Pasajero no encontrado')

    return result

@pasajero_api.delete('/{id}', status_code=204)
def borrar(id:int, db:Session = Depends(get_db)):
    result = pasajero_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pasajero no encontrado')

    return