# Supply

Codex CLI catalogue assistant with structured output and server-validated prices and stock.

![Interface](docs/preview.png)

[Validation notes](docs/VALIDATION.md) · [Source license](LICENSE)

## What it does

Покупатель - Codex CLI (gpt-6.1-sol) - SKU и количество - проверка остатков - серверный расчёт предложения.

Buyer - Codex CLI (gpt-6.1-sol) - structured SKU selection - stock validation - server-calculated quote.

Independent portfolio demo, written from scratch. Synthetic examples only. No commercial source, proprietary prompts, client recordings or customer data.

## Run locally

Python 3.12, Node 22 and pnpm 11.19.0:

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pnpm install --frozen-lockfile
pnpm build
uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000. For UI development: `pnpm dev` (API proxy expects port 8000).

```sh
docker compose up --build
```

Local-only binding is deliberate. These demos have no user authentication and are not hardened multi-user hosted services.

## Checks and delivery

```sh
pip install pytest httpx
pytest -q
pnpm build
```

GitHub Actions runs backend checks, TypeScript/build checks and Docker image build. Model credentials are never included in CI or a public image.

## Boundaries

AI-диалог только для доверенных запросов локально. Shell и web tools отключены; это не доказательство полной изоляции CLI. Не публикуйте сервер с ENABLE_CODEX=1 без отдельной аутентификации, изоляции и ограничений. Нет 1С, оплаты и внешних заказов.

The full application runs locally with its Python backend. A static build alone cannot transcribe audio, execute workflows, render video or call Codex.

## Stack and attribution

Python / FastAPI / React / TypeScript / Vite / Motion / Lucide. Google Fonts: Golos Text (SIL OFL). All third-party dependencies retain their own licenses. See `THIRD_PARTY.md`.

MIT for independently authored source. Asset provenance and actual validation: `docs/VALIDATION.md`.

## Enable the actual Codex agent

Install the official Codex CLI and run `codex login` on your own computer. Existing subscription authentication is used; no API key is bundled.

PowerShell:
```powershell
$env:ENABLE_CODEX = '1'
$env:CODEX_BIN = 'C:\path\to\codex.exe'
uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

On Linux/macOS: `ENABLE_CODEX=1 uvicorn backend.app:app --host 127.0.0.1 --port 8000`.
The default Docker image deliberately does not include an authenticated Codex CLI. Its catalogue/quote endpoints work without model access.

Official integration reference: https://learn.chatgpt.com/docs/non-interactive-mode
