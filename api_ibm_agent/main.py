from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.chat import chat_api
from core.configs import settings


app = FastAPI(title='AskLAI API', description='Requisição para agente especialista em transparência municipal')
app.include_router(chat_api.api_router, prefix=settings.API_V1_STR, tags=['chat_api'])


# Configurar os domínios permitidos
origins = [
    "http://127.0.0.1:5500",  # Frontend local
    "http://localhost:5500",   # Outra forma de acessar
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Pode usar ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, PUT, DELETE, etc
    allow_headers=["*"],    # Headers permitidos
)



if __name__ == '__main__':
    import uvicorn    
    uvicorn.run("main:app", host='0.0.0.0', reload=True)