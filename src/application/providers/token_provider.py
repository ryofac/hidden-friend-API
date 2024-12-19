from abc import ABC, abstractmethod


class TokenProvider(ABC):
    @abstractmethod
    def encode(self, data: dict, expires: int) -> str:
        pass

    @abstractmethod
    def decode(self, token: str) -> str:
        pass
