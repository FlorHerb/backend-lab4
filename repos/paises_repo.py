from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.paises_bd import PaisBD
from modelos.ciudades_bd import CiudadBD
from modelos.paises import PaisSinId

class PaisRepo():
    def get_all(self, db:Session ):
        return db.execute(select(PaisBD, CiudadBD).join(CiudadBD, isouter=True)).scalars().all()
    
    def get_by_id(self, db: Session, id: int):
        result = db.execute(select(PaisBD).where(PaisBD.id == id)).scalar()
        return result

    def agregar(self, db:Session, datos:PaisSinId): 
        nueva_entidad: PaisBD = PaisBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        db.commit()
        return nueva_entidad

    def modificar(self, db:Session, id:int, datos:PaisSinId): 
        entidad:PaisBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:int):
        entidad:PaisBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad