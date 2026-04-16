from src.config.settings import settings
from src.providers.base import ProviderClient
from src.providers.gemini import GeminiClient
from src.providers.github_models import GitHubModelsClient
from src.providers.openai_compatible import OpenAICompatibleClient


def get_provider_client() -> ProviderClient:
    provider = settings.model_provider.lower().strip()

    if provider == "github":
        return GitHubModelsClient(
            endpoint=settings.github_models_endpoint,
            token=settings.github_models_token,
            auth_mode=settings.github_models_auth_mode,
            token_command=settings.github_models_token_command,
        )

    if provider == "gemini":
        return GeminiClient(api_key=settings.gemini_api_key)

    if provider == "openai_compatible":
        return OpenAICompatibleClient(
            base_url=settings.openai_compatible_base_url,
            api_key=settings.openai_compatible_api_key,
        )

    raise ValueError(
        "Unsupported MODEL_PROVIDER. "
        "Supported values: github, gemini, openai_compatible"
    )
