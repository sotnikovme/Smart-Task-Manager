from fastapi import APIRouter

from sqla.crud.OperationsWithUsers import create_user, update_user, find_user_by_id

router = APIRouter()


@router.post("/user_register/")
async def user_register(
        name: str,
        email: str,
        password: str
):
    await create_user(name=name, email=email, password=password)


@router.post("/user_update/")
async def user_update(
        user_id: int,
        # crud: UserUpdate,
        **kwargs
):
    await update_user(user_id=user_id, **kwargs)


@router.get("/user/{user_id}")
async def user_page(user_id: int):
    await find_user_by_id(user_id=user_id)