from typing import List, Optional
from pydantic import BaseModel


class ChatRequestSchema(BaseModel):
    messages: str
    stream: bool = False
    thread_id: Optional[str] = ''

class ChatResponseSchema(BaseModel):
    message: str
    thread_id: Optional[str]
    status_msg: str

class Content(BaseModel):
    response_type: str
    text: str


class Message(BaseModel):
    role: str
    content: List[Content]


class AgentMessage(BaseModel):
    messages: List[Message]
    stream: bool
