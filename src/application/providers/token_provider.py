from abc import ABC, abstractmethod


class TokenProvider(ABC):
    @abstractmethod
    def encode(self, data: str, expires: str) -> str:
        pass

    @abstractmethod
    def decode(self, token: str) -> str:
        pass
