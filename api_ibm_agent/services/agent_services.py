from core.configs import settings
from core.deps import token_manager
from schemas.agent_schema import AgentMessage, Content, Message

import aiohttp



async def send_message(input: str, thread_id: str) -> list:
    
    headers = {
        "Authorization": f"Bearer {token_manager.get_token()}",
        "Content-Type": "application/json"
    }

    if thread_id:
        headers['X-IBM-THREAD-ID'] = thread_id

    body = AgentMessage(
        messages=[
            Message(
                role="user",
                content=[
                    Content(
                        response_type="txt",
                        text=input
                    )
                ]
            )
        ],
        stream=False
    )

    async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{settings.ENDPOINT_IBM}/v1/orchestrate/{settings.AGENT_ID}/chat/completions',
                headers=headers,
                json=body.model_dump() # Serialização para enviar como JSON
            ) as response:
                data = await response.json()
                thread_identify = data.get('thread_id')
                choices = data.get('choices')[0]
                print(choices)
                messages = choices.get('message')
            return [messages.get('content'), thread_identify]
    
