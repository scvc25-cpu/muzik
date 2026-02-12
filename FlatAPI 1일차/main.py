from app.schemas.users import UserCreateRequest


@app.post("/users")
async def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return {"id": user.id}