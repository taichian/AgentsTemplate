from src.providers.base import ProviderClient


class OpenAICompatibleClient(ProviderClient):
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def chat(self, system_prompt: str, user_prompt: str, model: str) -> str:
        if not self.api_key:
            raise ValueError("Missing OPENAI_COMPATIBLE_API_KEY")
        prompt_preview = (
            f"System='{system_prompt[:80]}' "
            f"User='{user_prompt[:120]}'"
        )
        return (
            f"[openai-compatible:{model}] {prompt_preview} "
            "(stub response - replace with real API call)"
        )
