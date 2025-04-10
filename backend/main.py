from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from backend.langchain_helper import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    persona: str = Field(min_length=1)
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = get_response(request.persona, request.message)
    return JSONResponse(
        status_code=response[1],
        content=ChatResponse(response=response[0]).dict()
    )
