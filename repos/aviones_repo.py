from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.aviones_bd import AvionBD
from modelos.aviones import Avion

class AvionRepo():
    def get_all(self, db:Session ):
        return db.execute(select(AvionBD)).scalars().all()
    
    def get_by_id(self, db: Session, id: str):
        result = db.execute(select(AvionBD).where(AvionBD.id == id)).scalar()
        return result

    def agregar(self, db:Session, datos:Avion): 
        nueva_entidad: AvionBD = AvionBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        db.commit()
        return nueva_entidad

    def modificar(self, db:Session, id:str, datos:Avion): 
        entidad:AvionBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:str):
        entidad:AvionBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad