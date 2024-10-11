from fastapi import APIRouter
from app.ddd.infra.repository import *

router = APIRouter()

from app.ddd.infra.database import get_db

@router.get("/users/{user_id}", tags=["user"])
def get_user(user_id: str):
    # db: Session = Depends(get_db)
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    return user

@router.get("/query/users", tags=["user"])
def query_user(q: str = ""):
    user_repository = UserRepository()
    users = user_repository.query()
    return users
    return {"q": q}

@router.post("/users", tags=["user"])
def create_user(user: CreateUser):
    print(user)
    # user = User.model_validate(
    #     user
    # )
    user_repository = UserRepository()
    user = user_repository.insert(user)
    return user

@router.delete("/users/{user_id}", tags=["user"])
def delete_user(user_id: str):
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    user = user_repository.delete(user)
    return user
