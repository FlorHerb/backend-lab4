from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from repos.vuelos_repo import VueloRepo
from repos.asientos_repo import AsientoRepo
from modelos.asientos import AsientoSinCod
from modelos.vuelos import VueloSinCod, VueloConObj, Vuelo
from repos.aviones_repo import AvionRepo
from modelos.aviones import Avion
from datetime import date

vuelo_api = APIRouter(prefix='/vuelos', tags=['vuelos'])
vuelo_repo = VueloRepo()
asientos_repo = AsientoRepo()
avion_repo= AvionRepo()

@vuelo_api.get('', response_model=list[VueloConObj])
def get_all(db:Session = Depends(get_db)):
    result = vuelo_repo.get_all(db)
    return result

@vuelo_api.get('/{id}', response_model=VueloConObj)
def get_by_id(id: str, db:Session = Depends(get_db)):
    result = vuelo_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Vuelo no encontrado')
    return result

@vuelo_api.get('/{cod_origen}/{fecha1}/{fecha2}', response_model=list[VueloConObj])
def get_filtrado(cod_origen:str, fecha1:date, fecha2:date, db:Session = Depends(get_db)):
    result= vuelo_repo.get_filtrado(db,cod_origen,fecha1,fecha2)
    if result is None:
        raise HTTPException(status_code=404, detail='Vuelos no encontrados')
    

@vuelo_api.post('', response_model=Vuelo, status_code=201)
def nuevo(datos:Vuelo, db:Session = Depends(get_db)):
    result = vuelo_repo.agregar(db, datos)
    if result is None:
        raise HTTPException(status_code=400,detail='Error en los datos del vuelo (código o fecha de salida incorrectos)')
    avion: Avion=avion_repo.get_by_id(db,datos.cod_avion)
    asiento:AsientoSinCod = AsientoSinCod(num_asiento=0,cod_vuelo='CCC',id_pasaje=None)
    for i in range(1,avion.capacidad+1):
        asiento.num_asiento=i
        asiento.cod_vuelo=datos.codigo
        asiento.id_pasaje=None
        asientos_repo.agregar(db,asiento)
        
    return result


@vuelo_api.put('/{id}', response_model=VueloConObj)
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