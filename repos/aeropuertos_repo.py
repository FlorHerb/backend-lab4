from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.aeropuertos_bd import AeropuertoBD
from modelos.ciudades_bd import CiudadBD
from modelos.aeropuertos import Aeropuerto

class AeropuertoRepo():
    def get_all(self, db:Session ):
        return db.execute(select(AeropuertoBD, CiudadBD).join(CiudadBD, isouter=True)).scalars().all()
    
    def get_by_id(self, db: Session, id: str):
        result = db.execute(select(AeropuertoBD).where(AeropuertoBD.id == id)).scalar()
        return result

    def agregar(self, db:Session, datos:Aeropuerto): 
        nueva_entidad: AeropuertoBD = AeropuertoBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        db.commit()
        return nueva_entidad

    def modificar(self, db:Session, id:str, datos:Aeropuerto): 
        entidad:AeropuertoBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:str):
        entidad:AeropuertoBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad