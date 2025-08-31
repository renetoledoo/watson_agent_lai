import time
import requests
from pydantic import BaseModel


class IBMToken(BaseModel):
    access_token: str
    expires_in: int
    token_type: str


class IBMTokenManager:
    def __init__(self, api_key: str, auth_url: str):
        self.api_key = api_key
        self.auth_url = auth_url
        self.token: IBMToken | None = None
        self.expire_at: float = 0

    def get_token(self) -> str:
        if self.token and time.time() < self.expire_at:
            return self.token.access_token

        resp = requests.post(
            self.auth_url,
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": self.api_key,
            },
        )
        webservice = resp.json()

        token = IBMToken(
            access_token= webservice.get('access_token'),
            expires_in= int(webservice.get('expires_in')),
            token_type= webservice.get('token_type'),
        )
        
        return token.access_token
