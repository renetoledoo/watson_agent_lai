from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = '/api/chat'
    ENDPOINT_IBM: str = config('ENDPOINT')
    AGENT_ID: str = config('AGENT_ID')
    SECRET_VERIFY: str = config('IBM_APIKEY')
    ENDPOINT_JWT: str = config('ENDPOINT_TOKEN')


settings: Settings = Settings()