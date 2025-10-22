from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Blog service funcionando correctamente"}

@app.get("/posts")
def get_posts():
    return [
        {"id": 1, "title": "Primer post", "content": "Contenido del primer post"},
        {"id": 2, "title": "Segundo post", "content": "Contenido del segundo post"},
        {"id": 3, "title": "Tercer post", "content": "Contenido del tercer post"},
    ]
