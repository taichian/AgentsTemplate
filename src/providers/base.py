from abc import ABC, abstractmethod


class ProviderClient(ABC):
    @abstractmethod
    def chat(self, system_prompt: str, user_prompt: str, model: str) -> str:
        raise NotImplementedError
