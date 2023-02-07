from database import BaseBd
from sqlalchemy import Column,String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

class VueloBD(BaseBd):
    __tablename__ = 'vuelos'
    codigo= Column(String(5), primary_key=True)
    fecha = Column(Date, nullable=False)
    hora= Column(Time, nullable=False)
    cod_origen_aero= Column(String(4), ForeignKey('aeropuertos.codigo', onupdate="CASCADE", ondelete="CASCADE"))
    cod_destino_aero= Column(String(4), ForeignKey('aeropuertos.codigo', onupdate="CASCADE", ondelete="CASCADE"))
    cod_avion = Column(String(3), ForeignKey('aviones.codigo', onupdate="CASCADE", ondelete="CASCADE"))
    avion= relationship('AvionBD',back_populates='vuelos',cascade='save-update')
    origen_aero= relationship('AeropuertoBD',foreign_keys='VueloBD.cod_origen_aero')
    destino_aero=relationship('AeropuertoBD',foreign_keys='VueloBD.cod_destino_aero')
    pasajes= relationship('PasajeBD', cascade="all, delete-orphan")
    asientos= relationship('AsientoBD', cascade="all, delete-orphan")
    
    
    #origen_aero= relationship('AeropuertoBD', primaryjoin="AeropuertoBD.codigo==VueloBD.cod_origen_aero")
    #destino_aero=relationship('AeropuertoBD', primaryjoin="AeropuertoBD.codigo==VueloBD.cod_destino_aero")
    
    #billing_address = relationship("Address", foreign_keys=[billing_address_id])
    #shipping_address = relationship("Address", foreign_keys=[shipping_address_id])
    
   # from_account: Account = Relationship(sa_relationship_kwargs=dict(foreign_keys="[Transaction.from_account_id]"))

    
   