from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.asientos import Asiento
from repos.asientos_repo import AsientoRepo

asiento_api = APIRouter(prefix='/asientos', tags=['asientos'])
asiento_repo = AsientoRepo()

@asiento_api.get('', response_model=list[Asiento])
def get_all(db:Session = Depends(get_db)):
    result = asiento_repo.get_all(db)
    return result

@asiento_api.get('/{cod}', response_model=Asiento)
def get_by_vuelo(cod: str, db:Session = Depends(get_db)):
    result = asiento_repo.get_by_id(db, cod)
    if result is None:
        raise HTTPException(status_code=404, detail='Asiento no encontrado')
    return result




@asiento_api.post('', response_model=Asiento, status_code=201)
def nuevo(datos:Asiento, db:Session = Depends(get_db)):
    result = asiento_repo.agregar(db, datos)
    return result


@asiento_api.put('/{id}', response_model=Asiento)
def modificar(id:int, datos:Asiento, db:Session = Depends(get_db)):
    result = asiento_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Asiento no encontrado')

    return result

@asiento_api.delete('/{id}', status_code=204)
def borrar(id:int, db:Session = Depends(get_db)):
    result = asiento_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Asiento no encontrado')

    return