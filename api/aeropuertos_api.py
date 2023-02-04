from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.aeropuertos import Aeropuerto
from repos.aeropuertos_repo import AeropuertoRepo
from modelos.aeropuertos import AeropuertoSinCod

aeropuerto_api = APIRouter(prefix='/aeropuertos', tags=['Aeropuertos'])
aeropuerto_repo = AeropuertoRepo()

@aeropuerto_api.get('', response_model=list[Aeropuerto])
def get_all(db:Session = Depends(get_db)):
    result = aeropuerto_repo.get_all(db)
    return result

@aeropuerto_api.get('/{id}', response_model=Aeropuerto)
def get_by_id(id: str, db:Session = Depends(get_db)):
    result = aeropuerto_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Aeropuerto no encontrado')
    return result

@aeropuerto_api.post('', response_model=Aeropuerto, status_code=201)
def nuevo(datos:AeropuertoSinCod, db:Session = Depends(get_db)):
    result = aeropuerto_repo.agregar(db, datos)
    if result is None:
        raise HTTPException(status_code=400,detail='El largo del código es incorrecto')
    return result


@aeropuerto_api.put('/{id}', response_model=Aeropuerto)
def modificar(id:str, datos:AeropuertoSinCod, db:Session = Depends(get_db)):
    result = aeropuerto_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Aeropuerto no encontrado')

    return result

@aeropuerto_api.delete('/{id}', status_code=204)
def borrar(id:str, db:Session = Depends(get_db)):
    result = aeropuerto_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Aeropuerto no encontrado')

    return