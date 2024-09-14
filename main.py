from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from databases import Database
from pydantic_settings import BaseSettings, SettingsConfigDict

# Configuración de la base de datos a través de las variables de entorno
class Settings(BaseSettings):
    database_url: str
    model_config = SettingsConfigDict(env_file=".env")

# Instancia de configuración
settings = Settings()

# Conexión a la base de datos
database = Database(settings.database_url)

# Configuración de SQLAlchemy
Base = declarative_base()
engine = create_engine(settings.database_url.replace('asyncpg', 'psycopg2'))  # Sincronizado para SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir el modelo de usuario en la base de datos
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Esquemas Pydantic para validación y respuesta
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Instancia de la aplicación FastAPI
app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para crear un usuario
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Endpoint para obtener todos los usuarios
@app.get("/users/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
