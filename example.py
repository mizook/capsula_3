from fastapi import FastAPI

# Instancia de la aplicación FastAPI
app = FastAPI()

# Endpoint para obtener todos los usuarios
@app.get("/helloworld/")
async def get_message():
    return "Hello World"