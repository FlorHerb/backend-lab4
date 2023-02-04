from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.vuelos_bd import VueloBD
from modelos.vuelos import Vuelo
from modelos.aeropuertos_bd import AeropuertoBD
from modelos.aviones_bd import AvionBD

class VueloRepo():
    def get_all(self, db:Session ):
        return db.execute(select(VueloBD, AeropuertoBD, AvionBD)
                          .join(AeropuertoBD, isouter=True)
                          .join(AeropuertoBD, isouter=True)
                          .join(AvionBD,isouter=True)).scalars().all()
    
    def get_by_id(self, db: Session, id: str):
        result = db.execute(select(VueloBD).where(VueloBD.id == id)).scalar()
        return result

    def agregar(self, db:Session, datos:Vuelo): 
        nueva_entidad: VueloBD = VueloBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        db.commit()
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