from pathlib import Path

from src.config.settings import settings
from src.core.markdown_loader import load_agent_markdown_bundle
from src.providers.factory import get_provider_client


class AgentRunner:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.client = get_provider_client()

    def run(self, user_message: str) -> str:
        bundle = load_agent_markdown_bundle(self.project_root)

        system_prompt = (
            "Follow workspace guidance and "
            "agent role definitions strictly.\n\n"
            f"Workspace instructions:\n{bundle['workspace_instruction']}\n\n"
            f"Agent definition:\n{bundle['agent_definition']}\n\n"
            f"Prompt template:\n{bundle['prompt_template']}"
        )

        return self.client.chat(
            system_prompt=system_prompt,
            user_prompt=user_message,
            model=settings.model_name,
        )
