from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    email: str

@app.post("/register")
def register(user: User):
    return {
        "message": f"Welcome {user.name}",
        "email": user.email
    }

@app.get("/getting")
def register():
    return {
        "message": f"Welcome"
    }