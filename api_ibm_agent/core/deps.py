from core.auth import IBMTokenManager
from core.configs import settings

print(f'[!] Obtendo Token de Acessso......')
token_manager = IBMTokenManager(
    api_key=settings.SECRET_VERIFY,
    auth_url=settings.ENDPOINT_JWT
)
print(f'[!] Token Criado: {token_manager.api_key}')