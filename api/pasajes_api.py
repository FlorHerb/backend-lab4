from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.pasajes import Pasaje
from repos.pasajes_repo import PasajeRepo
from modelos.pasajes import PasajeSinCod
from repos.asientos_repo import AsientoRepo


pasaje_api = APIRouter(prefix='/pasajes', tags=['pasajes'])
pasaje_repo = PasajeRepo()
asiento_repo = AsientoRepo()

@pasaje_api.get('', response_model=list[Pasaje])
def get_all(db:Session = Depends(get_db)):
    result = pasaje_repo.get_all(db)
    return result

@pasaje_api.get('/{id}', response_model=Pasaje)
def get_by_id(id: int, db:Session = Depends(get_db)):
    result = pasaje_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pasaje no encontrado')
    return result

@pasaje_api.post('', response_model=Pasaje, status_code=201)
def nuevo(datos:PasajeSinCod, db:Session = Depends(get_db)):
    result = pasaje_repo.agregar(db, datos)
    if result != None:
        asiento = asiento_repo.modif_por_pasaje(db, result.id, result.nro_asiento, result.cod_vuelo)
    return result


@pasaje_api.put('/{id}', response_model=Pasaje)
def modificar(id:int, datos:Pasaje, db:Session = Depends(get_db)):
    result = pasaje_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Pasaje no encontrado')

    return result

@pasaje_api.delete('/{id}', status_code=204)
def borrar(id:int, db:Session = Depends(get_db)):
    asiento_repo.modif_borrar_pasaje(db,id)
    result = pasaje_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pasaje no encontrado')
    return