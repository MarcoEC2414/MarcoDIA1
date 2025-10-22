from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Auth service funcionando correctamente"}

@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "1234":
        return {"status": "ok", "token": "abc123"}
    return {"status": "error", "message": "Credenciales inválidas"}
