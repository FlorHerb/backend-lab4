from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.pasajeros_bd import PasajeroBD
from modelos.pasajeros import Pasajero

class PasajeroRepo():
    def get_all(self, db:Session):
        return db.execute(select(PasajeroBD).order_by(PasajeroBD.nombre)).scalars().all()
    
    def get_by_id(self, db: Session, id: int):
        result = db.execute(select(PasajeroBD).where(PasajeroBD.dni == id)).scalar()
        return result

    def agregar(self, db:Session, datos:Pasajero): 
        nueva_entidad: PasajeroBD = PasajeroBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        db.commit()
        return nueva_entidad

    def modificar(self, db:Session, id:int, datos:Pasajero): 
        entidad:PasajeroBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:int):
        entidad:PasajeroBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad