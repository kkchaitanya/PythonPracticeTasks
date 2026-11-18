from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "Docker is running my FastAPI application"
    }
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }