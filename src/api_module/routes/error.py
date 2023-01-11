from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

error_router = APIRouter()

class Error(BaseModel):
    msg:str

def raise_error(request:Request, status_code:int, msg:str):
    headers = { "accept": "application/json", "x-header-error": msg.replace("\n", ", ") }

    if status_code == 401:
        return exeption_unauthorized(headers,msg)

    if status_code == 403:
        return exception_forbidden(headers,msg)

    if status_code == 404:
        return exception_not_found(headers,msg)

@error_router.get("/401")
@error_router.get("/401/", include_in_schema = False)
def exeption_unauthorized(headers:str, msg:str):
    msg = "Unauthorized"
    return HTTPException(status_code=401,detail=msg,headers=headers)


@error_router.get('/403')
@error_router.get('/403/', include_in_schema=False)
def exception_forbidden(headers:str, msg: str):
    return HTTPException(status_code=403, detail=msg, headers=headers)



@error_router.get('/404')
@error_router.get('/404/', include_in_schema=False)
def exception_not_found(headers:str, msg: str):
    return HTTPException(status_code=404, detail=msg, headers=headers)