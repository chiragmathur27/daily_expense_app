from fastapi import APIRouter, HTTPException
from app.models import User
from app.database import database

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: User):
    if await database.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    await database.users.insert_one(user.dict())
    return user

@router.get("/users/{email}", response_model=User)
async def get_user(email: str):
    user = await database.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)