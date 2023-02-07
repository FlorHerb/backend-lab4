from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos.asientos_bd import AsientoBD
from modelos.asientos import AsientoSinCod
from modelos.pasajes_bd import PasajeBD

class AsientoRepo():
    def get_all(self, db:Session):
        return db.execute(select(AsientoBD, PasajeBD).join(PasajeBD, isouter=True)).scalars().all()
    
    def get_by_vuelo(self, db:Session, cod_vuelo:str):
        result= db.execute(select(AsientoBD, PasajeBD).join(PasajeBD, isouter=True).where(AsientoBD.cod_vuelo == cod_vuelo).order_by(AsientoBD.num_asiento)).scalars().all()
        return result

    
    def get_by_id(self, db: Session, id: int):
        result = db.execute(select(AsientoBD).where(AsientoBD.id == id)).scalar()
        return result

    def agregar(self, db:Session, datos:AsientoSinCod): 
        nueva_entidad: AsientoBD = AsientoBD(**datos.dict()) #devuelve todos los atributos del objeto como un diccionario. el ** es para asignar los elementos de datos a nueva_entidad
        db.add(nueva_entidad)
        db.commit()
        return nueva_entidad

    def modificar(self, db:Session, id:int, datos:AsientoSinCod): 
        entidad:AsientoBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        for nom,val in datos.dict(exclude_unset=True).items():
            setattr(entidad,nom,val)
        db.commit()
        return entidad

    def borrar(self, db:Session, id:int):
        entidad:AsientoBD = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad
    
    def modif_por_pasaje(self, db:Session, pasaje_id:int, nro_asiento:int, cod_vuelo:str):
        entidad:AsientoBD =  db.execute(select(AsientoBD)
                                        .where(AsientoBD.cod_vuelo == cod_vuelo, 
                                      AsientoBD.num_asiento == nro_asiento)).scalar()
        if entidad is None:
            return None
        setattr(entidad,"id_pasaje",pasaje_id)
        db.commit()   
        return entidad
    
    def modif_borrar_pasaje(self, db:Session, id_pasaje:int):
        entidad:AsientoBD = db.execute(select(AsientoBD).where(AsientoBD.id_pasaje == id_pasaje)).scalar()
        if entidad is None:
            return None
        setattr(entidad,"id_pasaje",None)
        db.commit()   
        return entidad
        
    
    
    