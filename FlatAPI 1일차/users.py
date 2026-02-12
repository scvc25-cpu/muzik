from fastapi import HTTPException


@app.get("/users")
async def get_all_users():
    users = UserModel.all()

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    return [
        {
            "id": user.id,
            "username": user.username,
            "age": user.age,
            "gender": user.gender,
        }
        for user in users
    ]