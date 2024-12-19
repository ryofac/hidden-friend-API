import bcrypt
from bcrypt import hashpw

from application.providers.hash_provider import HashProvider


class BCryptHashProvider(HashProvider):
    def hash(self, payload: str) -> str:
        bytes_payload = payload.encode("utf-8")
        return hashpw(bytes_payload, bcrypt.gensalt())

    def verify(self, hashed: str, payload: str) -> bool:
        hashed_password = self.hash(payload)

        print(hashed_password)
        print(hashed)
        return hashed == hashed_password
