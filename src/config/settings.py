from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    model_provider: str = "github"
    model_name: str = "gpt-4o-mini"

    github_models_endpoint: str = "https://models.inference.ai.azure.com"
    github_models_token: str = ""
    github_models_auth_mode: str = "token"
    github_models_token_command: str = "gh auth token"

    gemini_api_key: str = ""

    openai_compatible_api_key: str = ""
    openai_compatible_base_url: str = "https://api.openai.com/v1"

    app_host: str = "0.0.0.0"
    app_port: int = 8000


settings = Settings()
