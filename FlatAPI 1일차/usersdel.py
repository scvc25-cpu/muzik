@app.delete("/users/{user_id}")
async def delete_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.delete()

    return {"detail": f"User: {user_id}, Successfully Deleted."}
