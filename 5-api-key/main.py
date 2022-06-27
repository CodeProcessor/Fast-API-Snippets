import json
import os

from fastapi import FastAPI
from fastapi import Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI(
    title="FAST API - Security"
)


def get_api_key_dict():
    try:
        value = os.getenv("API_KEY_DICT")
        _dict = json.loads(value)
        if not isinstance(_dict, dict):
            raise AttributeError("API_KEY_DICT is not a dictionary")
    except (AttributeError, TypeError) as _:
        print("API KEY DICT set to default")
        _dict = {"123": "Admin", "321": "User"}
    return _dict


ENABLE_AUTH = True
API_KEY_DICT = get_api_key_dict()
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_user(
        api_key: str = Security(api_key_header),
):
    if api_key in API_KEY_DICT.keys():
        return API_KEY_DICT[api_key]
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials, check your api key"
        )


@app.get("/")
async def homepage():
    return "Welcome to the security test!"


@app.get("/secure_endpoint", tags=["test"])
async def get_open_api_endpoint(username=Depends(get_user) if ENABLE_AUTH else ""):
    response = f"Welcome back {username}!"
    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
