import os


def test_provider_env_value_is_supported():
    supported = {"github", "gemini", "openai_compatible"}
    configured = os.getenv("MODEL_PROVIDER", "github")
    assert configured in supported
