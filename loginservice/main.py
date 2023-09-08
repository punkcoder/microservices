from fastapi import FastAPI

from models import User

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/register")
async def register(user: User):
    return {"message": "User registered successfully"}
