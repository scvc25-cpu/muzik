from fastapi import Path


@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "username": user.username,
        "age": user.age,
        "gender": user.gender,
    }