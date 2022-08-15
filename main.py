from fastapi import FastAPI

app = FastAPI(title= "Live de CF", description="Prueba de FastAPI", version= "1.0.1")

@app.get('/')
async def index():
    return "Hola mundo"

@app.get('/about')
async def about():
    return "Ayuda desde FastAPI servicio web"