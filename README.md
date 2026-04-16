# Custom Agent Starter (Simple)

A simple, markdown-driven starter repo for custom agents with pluggable model providers.

- Provider selection supported: GitHub Models, Gemini, and OpenAI-compatible endpoints.
- Agent behavior setup supported through markdown files in `.github/`.
- Includes basic CI and staging deployment workflow.

## 1. Prerequisites

Install:

- Python 3.10+
- Git
- Docker Desktop (for container/local compose workflow)

Accounts/tokens:

- GitHub token for GitHub Models (if using `MODEL_PROVIDER=github`)
- Optional: GitHub CLI SSO session (for GitHub provider with `gh_cli_sso`)
- Gemini API key (if using `MODEL_PROVIDER=gemini`)
- OpenAI-compatible API key and endpoint (if using `MODEL_PROVIDER=openai_compatible`)

## 2. Clone and install dependencies

```bash
git clone <your-repo-url>
cd notebooks
python -m venv .venv
# Windows cmd
.venv\Scripts\activate
pip install -U pip
pip install -e .
```

## 3. Configure environment

Create `.env` from the template:

```bash
copy .env.example .env
```

Open `.env` and set:

- `MODEL_PROVIDER` to one of: `github`, `gemini`, `openai_compatible`
- `MODEL_NAME` to your selected model
- the matching provider credentials

### Provider options

1. GitHub Models

- `MODEL_PROVIDER=github`
- choose one credential mode:

  - static token mode: set `GITHUB_MODELS_AUTH_MODE=token` and `GITHUB_MODELS_TOKEN`
  - GitHub CLI SSO mode: set `GITHUB_MODELS_AUTH_MODE=gh_cli_sso` and `GITHUB_MODELS_TOKEN_COMMAND=gh auth token`

- optional endpoint override: `GITHUB_MODELS_ENDPOINT`
- full step-by-step template: `templates/github-copilot-sso.md`

1. Gemini

- `MODEL_PROVIDER=gemini`
- set `GEMINI_API_KEY`

1. OpenAI-compatible

- `MODEL_PROVIDER=openai_compatible`
- set `OPENAI_COMPATIBLE_API_KEY`
- set `OPENAI_COMPATIBLE_BASE_URL`

## 4. Set up agent behavior using markdown files

This starter uses `.md` files as the customization surface.

### 4.1 Workspace instructions

File: `.github/instructions/workspace.instructions.md`

Purpose:

- always-on guidance for coding and behavior
- shared team guardrails

How to edit:

1. Keep YAML frontmatter at the top between `---` markers.
2. Keep `description` explicit: include trigger phrase like `Use when:`.
3. Add clear do/don't bullets in the body.

### 4.2 Custom agent definition

File: `.github/agents/researcher.agent.md`

Purpose:

- define role behavior, responsibilities, and tool access

How to edit:

1. Keep `name` and `description` in frontmatter.
2. Set model/tool hints as needed.
3. Keep role instructions short and action-oriented.

### 4.3 Prompt template

File: `.github/prompts/summarize.prompt.md`

Purpose:

- define reusable prompt workflows with placeholders

How to edit:

1. Add frontmatter with `description` and mode.
2. Use placeholder variables like `{{source_text}}`.
3. State expected output format explicitly.

### 4.4 Skill package

File: `.github/skills/file-review/SKILL.md`

Purpose:

- define reusable multi-step workflow logic

How to edit:

1. Keep frontmatter `name` aligned with folder name.
2. Use `description` with trigger phrase (`Use when:`).
3. List deterministic steps in numbered order.

## 5. Run the app locally

```bash
uvicorn src.app.main:app --reload
```

Check health:

```bash
curl http://127.0.0.1:8000/health
```

Expected response includes active provider/model.

## 6. Test chat endpoint

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Summarize the current project setup."}'
```

## 7. Switch providers without code changes

1. Update `.env`:

- change `MODEL_PROVIDER`
- update matching credentials
- optionally update `MODEL_NAME`

1. Restart app.

1. Re-run `/health` and `/chat`.

If provider setup is correct, responses will show the new provider/model.

## 8. Run tests

```bash
pytest
```

## 9. CI/CD overview

- CI: `.github/workflows/ci.yml`

  install deps, run pytest

- CD: `.github/workflows/deploy-staging.yml`

  build and publish image, then deploy to staging

## 10. Deployment (simple path)

### Local container

```bash
docker build -f deployment/docker/Dockerfile -t custom-agent-starter:local .
docker run --env-file .env -p 8000:8000 custom-agent-starter:local
```

### Local compose

```bash
docker compose -f deployment/docker/docker-compose.yml up --build
```

### Staging Kubernetes

1. Ensure cluster credentials are configured.
2. Push image from CI.
3. Apply manifests:

```bash
kubectl apply -k deployment/k8s/overlays/staging
```

## 11. Troubleshooting

1. Auth errors

- verify token/key in `.env`
- ensure no leading/trailing spaces

1. Unsupported provider

- `MODEL_PROVIDER` must be `github`, `gemini`, or `openai_compatible`

1. Markdown customization not picked up

- verify exact file locations under `.github/`
- ensure YAML frontmatter is valid

1. Skill discovery issues

- folder and frontmatter name should match skill identity
- description must include explicit trigger wording

## 12. Suggested next improvements

1. Replace provider stubs with real API calls.
2. Add request/response schemas and validation tests.
3. Add prod deployment workflow with manual approval and rollback.
