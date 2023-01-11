from fastapi import Request, APIRouter
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel
from typing import Optional

from src.chat.chat import chatbot_response

api_router = APIRouter()

class ChatStruct(BaseModel):
    message:str
    user: Optional[str]

@api_router.get("/api/chat")
@api_router.get("/api/chat/",include_in_schema=False)
async def chat(request:Request,data:ChatStruct):
    response = chatbot_response(data.message)
    return { "bot response": f"{response}" }
