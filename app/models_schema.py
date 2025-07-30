from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class Visualizacion(BaseModel):
    episodio_id: str  
    fecha: datetime

class User(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nombre: str
    visualizaciones: List[Visualizacion] = []

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        populate_by_name = True

class Episodio(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    numero: int
    titulo: str
    fecha_emision: datetime
    director_id: str


class Temporada(BaseModel):
    numero: int
    anio: int
    episodios: List[Episodio]

class Actor(BaseModel):
    persona_id: str 
    personaje: str

class Serie(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    titulo: str
    genero: str
    anio_inicio: int
    anio_fin: Optional[int] = None
    creadores: List[str]
    actores: List[Actor]
    temporadas: List[Temporada]

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        populate_by_name = True


class Rol(BaseModel):
    tipo: str
    serie_id: str 
    personaje: Optional[str]

class Persona(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nombre: str
    fecha_nacimiento: Optional[datetime] = None
    nacionalidad: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        populate_by_name = True

