from pydantic import conint


class UserSearchParams(BaseModel):
    model_config = {"extra": "forbid"}  # 다른 쿼리 파라미터 허용하지 않음

    username: str | None = None
    age: conint(gt=0) | None = None
    gender: GenderEnum | None = None

from typing import Annotated
from fastapi import Query
from app.schemas.users import UserSearchParams


@app.get("/users/search")
async def search_users(
    query_params: Annotated[UserSearchParams, Query()]
):
    valid_query = {
        key: value
        for key, value in query_params.model_dump().items()
        if value is not None
    }

    filtered_users = UserModel.filter(**valid_query)

    if not filtered_users:
        raise HTTPException(status_code=404, detail="No matching users found")

    return [
        {
            "id": user.id,
            "username": user.username,
            "age": user.age,
            "gender": user.gender,
        }
        for user in filtered_users
    ]
