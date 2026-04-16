from src.providers.base import ProviderClient


class GeminiClient(ProviderClient):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def chat(self, system_prompt: str, user_prompt: str, model: str) -> str:
        if not self.api_key:
            raise ValueError("Missing GEMINI_API_KEY")
        prompt_preview = (
            f"System='{system_prompt[:80]}' "
            f"User='{user_prompt[:120]}'"
        )
        return (
            f"[gemini:{model}] {prompt_preview} "
            "(stub response - replace with real API call)"
        )
