# Запуск и разработка

Для запуска без Docker нужны Python 3.12, Node.js 22 и pnpm 11.19.0. Команды выполняются из корня проекта.

## Windows / PowerShell

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
pnpm install --frozen-lockfile
pnpm build
.venv\Scripts\python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

## Linux / macOS

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
pnpm install --frozen-lockfile
pnpm build
.venv/bin/python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

Интерфейс доступен по адресу http://localhost:8000. Для разработки интерфейса запустите `pnpm dev` в отдельном терминале; API должен продолжать работать на порту 8000.

## Проверки

```sh
python -m pip install pytest httpx
python -m pytest -q
pnpm build
```

Команды `python` должны использовать созданное виртуальное окружение. GitHub Actions проверяет серверную часть, TypeScript, сборку интерфейса и сборку Docker-образа.

## Данные

Локальные файлы сохраняются в `data/`, которая исключена из Git. Docker Compose подключает эту же папку к контейнеру. На Linux владелец папки должен разрешить запись пользователю контейнера с UID 1000. Приложение предназначено для локального запуска и не содержит авторизации пользователей.

## Подключение помощника

Установите официальный Codex CLI и выполните `codex login` на своём компьютере. Затем запустите сервер:

```powershell
$env:ENABLE_CODEX = '1'
$env:CODEX_BIN = 'C:\путь\к\codex.exe'
.venv\Scripts\python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

Для Linux/macOS, если `codex` доступен в PATH:

```sh
ENABLE_CODEX=1 .venv/bin/python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

Модель по умолчанию - `gpt-6.1-sol`. Docker-образ не содержит авторизованного Codex CLI; в нём доступны каталог и расчёт предложения. Режим с помощником предназначен для доверенных локальных запросов: он не является изолированным публичным агентом.

## Снимки интерфейса

Для снимков интерфейса используйте `/?preview`: полосы прокрутки скрыты, прокрутка сохраняется. В обычном режиме полосы доступны.
