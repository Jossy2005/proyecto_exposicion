from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola bienvenido a nuestra prueba de Kubernetes con CI/CD automatizado!"}

@app.get("/status")
def status():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
