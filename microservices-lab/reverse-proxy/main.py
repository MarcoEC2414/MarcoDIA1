from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Reverse proxy funcionando correctamente"}
