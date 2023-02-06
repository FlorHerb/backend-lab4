from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.pasajes_bd import PasajeBD
from modelos.pasajes import PasajeSinCod
from modelos.pasajeros_bd import PasajeroBD

class PasajeRepo():
    def get_all(self, db:Session ):
        return db.execute(select(PasajeBD, PasajeroBD).join(PasajeroBD, isouter=True)).scalars().all()
    
    def get_by_id(self, db: Session, id: int):
        result = db.execute(select(PasajeBD).where(PasajeBD.id == id)).scalar()
        return result

    def agregar(self, db:Session, datos:PasajeSinCod): 
        nueva_entidad: PasajeBD = PasajeBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        
        db.commit()
        return nueva_entidad

    def modificar(self, db:Session, id:int, datos:PasajeSinCod): 
        entidad:PasajeBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:int):
        entidad:PasajeBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad
    
    