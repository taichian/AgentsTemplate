from pathlib import Path
from typing import Dict


def _read_markdown(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def load_agent_markdown_bundle(project_root: Path) -> Dict[str, str]:
    instruction_path = (
        project_root
        / ".github"
        / "instructions"
        / "workspace.instructions.md"
    )
    agent_path = project_root / ".github" / "agents" / "researcher.agent.md"
    prompt_path = project_root / ".github" / "prompts" / "summarize.prompt.md"

    return {
        "workspace_instruction": _read_markdown(instruction_path),
        "agent_definition": _read_markdown(agent_path),
        "prompt_template": _read_markdown(prompt_path),
    }
