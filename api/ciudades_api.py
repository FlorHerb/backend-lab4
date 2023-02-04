from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.ciudades import Ciudad
from repos.ciudades_repo import CiudadRepo
from modelos.ciudades import CiudadSinId

ciudad_api = APIRouter(prefix='/ciudades', tags=['ciudades'])
ciudad_repo = CiudadRepo()

@ciudad_api.get('', response_model=list[Ciudad])
def get_all(db:Session = Depends(get_db)):
    result = ciudad_repo.get_all(db)
    return result

@ciudad_api.get('/{id}', response_model=Ciudad)
def get_by_id(id: int, db:Session = Depends(get_db)):
    result = ciudad_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Ciudad no encontrada')
    return result

@ciudad_api.post('', response_model=Ciudad, status_code=201)
def nuevo(datos:CiudadSinId, db:Session = Depends(get_db)):
    result = ciudad_repo.agregar(db, datos)
    return result


@ciudad_api.put('/{id}', response_model=Ciudad)
def modificar(id:int, datos:Ciudad, db:Session = Depends(get_db)):
    result = ciudad_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Ciudad no encontrada')

    return result

@ciudad_api.delete('/{id}', status_code=204)
def borrar(id:int, db:Session = Depends(get_db)):
    result = ciudad_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Ciudad no encontrada')

    return