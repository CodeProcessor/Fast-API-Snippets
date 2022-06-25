from fastapi import FastAPI
from fastapi import Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI(
    title="FAST API - Security"
)

API_KEY_DICT = {
    "123": "Admin",
    "111": "User",
}
API_KEY_NAME = "access_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_user(
        api_key: str = Security(api_key_header),
):
    if api_key in API_KEY_DICT.keys():
        return API_KEY_DICT[api_key]
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


@app.get("/")
async def homepage():
    return "Welcome to the security test!"


@app.get("/secure_endpoint", tags=["test"])
async def get_open_api_endpoint(username=Depends(get_user)):
    response = f"How cool is this? - {username}"
    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
