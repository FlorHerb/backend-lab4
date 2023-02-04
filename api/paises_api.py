from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.paises import Pais
from repos.paises_repo import PaisRepo
from modelos.paises import PaisSinId

pais_api = APIRouter(prefix='/Paises', tags=['Paises'])
pais_repo = PaisRepo()

@pais_api.get('', response_model=list[Pais])
def get_all(db:Session = Depends(get_db)):
    result = pais_repo.get_all(db)
    return result

@pais_api.get('/{id}', response_model=Pais)
def get_by_id(id: int, db:Session = Depends(get_db)):
    result = pais_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pais no encontrado')
    return result

@pais_api.post('', response_model=Pais, status_code=201)
def nuevo(datos:PaisSinId, db:Session = Depends(get_db)):
    result = pais_repo.agregar(db, datos)
    return result


@pais_api.put('/{id}', response_model=Pais)
def modificar(id:int, datos:Pais, db:Session = Depends(get_db)):
    result = pais_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Pais no encontrado')

    return result

@pais_api.delete('/{id}', status_code=204)
def borrar(id:int, db:Session = Depends(get_db)):
    result = pais_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pais no encontrado')

    return