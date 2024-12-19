import datetime

from jose import jwt

from application.providers.token_provider import TokenProvider


class JoseTokenProvider(TokenProvider):
    def encode(self, data: dict, expires_in_seconds: int) -> str:
        expiration_time = datetime.utcnow() + datetime.timedelta(
            seconds=expires_in_seconds
        )
        payload = {**data, "exp": expiration_time}
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode(self, token: str) -> str:
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado.")
        except jwt.JWTError as e:
            raise ValueError(f"Erro ao decodificar o token: {str(e)}")
