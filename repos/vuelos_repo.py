from sqlalchemy.orm import Session
from sqlalchemy import select, between
from modelos.vuelos_bd import VueloBD
from modelos.vuelos import Vuelo
from modelos.aeropuertos_bd import AeropuertoBD
from modelos.aviones_bd import AvionBD
from sqlalchemy.orm import aliased
from sqlalchemy.sql.expression import join
from datetime import date

class VueloRepo():
    def get_all(self, db:Session ):
        origen=aliased(AeropuertoBD)
        destino=aliased(AeropuertoBD)
        return db.execute(select(VueloBD)
                         .outerjoin(origen, VueloBD.cod_origen_aero == origen.codigo)
                         .outerjoin(destino,VueloBD.cod_destino_aero == destino.codigo)
                         .outerjoin(AvionBD)).scalars().all()
      
      
    def get_by_id(self, db: Session, id: str):
        result = db.execute(select(VueloBD).where(VueloBD.codigo == id)).scalar()
        return result
    
    
    def get_filtrado(self, db: Session, cod_origen: str,fecha1: date, fecha2: date):
       result = db.execute(select(VueloBD).where(VueloBD.cod_origen_aero == "QQQQQ")).scalars().all()
       return result
        #result = db.execute(select(VueloBD, AeropuertoBD).outerjoin(AeropuertoBD, VueloBD.cod_origen_aero == cod_origen)).scalars().all()
       # return result
    #VueloBD.fecha.between(fecha1,fecha2)
    #.where(VueloBD.fecha.between(fecha1,fecha2))

    

    def agregar(self, db:Session, datos:Vuelo): 
        nueva_entidad: VueloBD = VueloBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        
        control:VueloBD = db.execute(select(VueloBD)
                                     .where(VueloBD.cod_origen_aero == nueva_entidad.cod_origen_aero
                                            ,VueloBD.fecha == nueva_entidad.fecha
                                            ,VueloBD.cod_avion == nueva_entidad.cod_avion)).scalar()
        if len(nueva_entidad.codigo) == 5 and control == None:
           db.add(nueva_entidad)
           db.commit() 
        else:
            nueva_entidad= None
        return nueva_entidad
    
    def modificar(self, db:Session, id:str, datos:Vuelo): 
        entidad:VueloBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:str):
        entidad:VueloBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad