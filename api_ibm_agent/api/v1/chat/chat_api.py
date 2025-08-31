from fastapi import APIRouter, status
from schemas.agent_schema import ChatRequestSchema, ChatResponseSchema

from services.agent_services import send_message

api_router = APIRouter()


@api_router.post('/', status_code= status.HTTP_200_OK)
async def processing_msg(message: ChatRequestSchema) -> ChatResponseSchema:
    """
    Processa uma mensagem enviada para o agente.

    Este endpoint recebe uma  mensagens e um thread_id, envia para o serviço
    de agente (`send_message`) e retorna a resposta do agente estruturada em ChatResponseSchema.
    """
    try:
        outuput = await send_message(message.messages, thread_id=message.thread_id)
        retorno: ChatResponseSchema = ChatResponseSchema(
            message=outuput[0],
            thread_id=outuput[1],
            status_msg='OK'
        )
        
        return retorno
        
    except:
        retorno: ChatResponseSchema = ChatResponseSchema(
                    message='ERROR',
                    thread_id='ERROR',
                    status_msg='Erro ao processar msg'
                )
                
        return retorno

@api_router.get('/')
async def get_status():
    """
    Verifica se o status da api está ok
    """
    return {'status': 'OK'}