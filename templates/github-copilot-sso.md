# GitHub Copilot SSO Credential Template

Use this template when your organization uses SSO and you want to source runtime credentials from your GitHub CLI session.

## 1. Sign in with GitHub CLI

```bash
gh auth login
```

Choose:

- GitHub.com
- HTTPS
- Login with a web browser

## 2. Authorize SSO for your org

After login, ensure your org SSO policy authorizes the session.

```bash
gh auth status
```

If the org requires SSO authorization, complete the browser prompt.

## 3. Configure runtime auth mode

In `.env`:

```env
MODEL_PROVIDER=github
MODEL_NAME=gpt-4o-mini
GITHUB_MODELS_AUTH_MODE=gh_cli_sso
GITHUB_MODELS_TOKEN_COMMAND=gh auth token
GITHUB_MODELS_TOKEN=
```

Notes:

- Leave `GITHUB_MODELS_TOKEN` empty when using `gh_cli_sso`.
- Keep `GITHUB_MODELS_AUTH_MODE=token` if you prefer static secrets.

## 4. Verify token retrieval

```bash
gh auth token
```

A non-empty token confirms the CLI session is ready.

## 5. Run the app

```bash
uvicorn src.app.main:app --reload
```

## 6. Quick health check

```bash
curl http://127.0.0.1:8000/health
```

## 7. Troubleshooting

- If `gh auth token` fails, run `gh auth login` again.
- If SSO is enforced, confirm org authorization in browser.
- If multiple GH accounts are configured, switch to the expected account and re-run `gh auth status`.
