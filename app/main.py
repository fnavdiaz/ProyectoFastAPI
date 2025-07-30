from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler

from models_schema import User, Serie, Persona
from database import users_collection, series_collection, personas_collection

from bson import ObjectId
from bson.errors import InvalidId

app = FastAPI(title="API de Gestión de Contenidos")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.post("/users", summary="Crear nuevo usuario")
async def create_user(user: User):
    user_dict = user.dict(by_alias=True, exclude_none=True)
    result = await users_collection.insert_one(user_dict)
    return {"id": str(result.inserted_id)}

@app.get("/users/{user_id}", summary="Obtener usuario por ID")
async def get_user(user_id: str):
    try:
        object_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID de usuario no válido")

    user = await users_collection.find_one({"_id": object_id})
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user["_id"] = str(user["_id"])
    return user


@app.post("/series", summary="Crear nueva serie")
async def create_serie(serie: Serie):
    serie_dict = serie.dict(by_alias=True, exclude_none=True)
    result = await series_collection.insert_one(serie_dict)
    return {"id": str(result.inserted_id)}

@app.get("/series/{serie_id}", summary="Obtener serie por ID")
async def get_serie(serie_id: str):
    try:
        object_id = ObjectId(serie_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID de serie no válido")

    serie = await series_collection.find_one({"_id": object_id})
    if not serie:
        raise HTTPException(status_code=404, detail="Serie no encontrada")

    serie["_id"] = str(serie["_id"])
    return serie



@app.post("/personas", summary="Crear nueva persona")
async def create_persona(persona: Persona):
    persona_dict = persona.dict(by_alias=True, exclude_none=True)
    result = await personas_collection.insert_one(persona_dict)
    return {"id": str(result.inserted_id)}

@app.get("/personas/{persona_id}", response_model=Persona, summary="Obtener persona por ID")
async def get_persona(persona_id: str):
    try:
        object_id = ObjectId(persona_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID de persona no válido")

    persona = await personas_collection.find_one({"_id": object_id})
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

    persona["_id"] = str(persona["_id"])  # Evita error de serialización
    return persona



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("Validation error:", exc.errors())
    return await request_validation_exception_handler(request, exc)
