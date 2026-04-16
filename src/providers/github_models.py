import shlex
import subprocess

from src.providers.base import ProviderClient


class GitHubModelsClient(ProviderClient):
    def __init__(
        self,
        endpoint: str,
        token: str,
        auth_mode: str = "token",
        token_command: str = "gh auth token",
    ):
        self.endpoint = endpoint
        self.token = token
        self.auth_mode = auth_mode
        self.token_command = token_command

    def _resolve_token(self) -> str:
        if self.token:
            return self.token

        if self.auth_mode != "gh_cli_sso":
            raise ValueError(
                "Missing GITHUB_MODELS_TOKEN. "
                "Set token directly or use GITHUB_MODELS_AUTH_MODE=gh_cli_sso"
            )

        try:
            result = subprocess.run(
                shlex.split(self.token_command),
                check=True,
                capture_output=True,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError) as exc:
            raise ValueError(
                "Failed to resolve token from GitHub CLI. "
                "Run 'gh auth login' and ensure SSO is authorized."
            ) from exc

        token = result.stdout.strip()
        if not token:
            raise ValueError(
                "GitHub CLI returned an empty token. "
                "Verify your GH CLI session and SSO authorization."
            )

        return token

    def chat(self, system_prompt: str, user_prompt: str, model: str) -> str:
        token = self._resolve_token()
        prompt_preview = (
            f"System='{system_prompt[:80]}' "
            f"User='{user_prompt[:120]}'"
        )
        return (
            f"[github:{model}] {prompt_preview} "
            f"(stub response - token length {len(token)})"
        )
