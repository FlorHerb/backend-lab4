import uvicorn
from fastapi import FastAPI
import database
from fastapi.middleware.cors import CORSMiddleware
from repos.aeropuertos_repo import AeropuertoRepo
from repos.asientos_repo import AsientoRepo
from repos.aviones_repo import AvionRepo
from repos.ciudades_repo import CiudadRepo
from repos.paises_repo import PaisRepo
from repos.pasajeros_repo import PasajeroRepo
from repos.pasajes_repo import PasajeRepo
from repos.vuelos_repo import VueloRepo
from api.aeropuertos_api import aeropuerto_api
from api.asientos_api import asiento_api
from api.aviones_api import avion_api
from api.ciudades_api import ciudad_api
from api.paises_api import pais_api
from api.pasajeros_api import pasajero_api
from api.pasajes_api import pasaje_api
from api.vuelos_api import vuelo_api

database.create_all()

app = FastAPI()
app.include_router(aeropuerto_api)
app.include_router(asiento_api)
app.include_router(avion_api)
app.include_router(ciudad_api)
app.include_router(pais_api)
app.include_router(pasajero_api)
app.include_router(pasaje_api)
app.include_router(vuelo_api)



origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    uvicorn.run('vuelos:app', host='127.0.0.1', port=8000, reload=True)