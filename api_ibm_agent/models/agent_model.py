from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ChatCompletion(Base):
    __tablename__ = "chat_completions"

    id = Column(String, primary_key=True)  # id do chat completion
    object_type = Column(String, nullable=False)  # ex: "chat.completion"
    created = Column(BigInteger, nullable=False)  # timestamp
    model = Column(String, nullable=False)  # modelo utilizado
    thread_id = Column(String, nullable=True)  # id da thread
