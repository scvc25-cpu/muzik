class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None

from app.schemas.users import UserUpdateRequest


@app.patch("/users/{user_id}")
async def update_user(
    data: UserUpdateRequest,
    user_id: int = Path(gt=0),
):
    user = UserModel.get(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.update(**data.model_dump())

    return {
        "id": user.id,
        "username": user.username,
        "age": user.age,
        "gender": user.gender,
    }