FROM node:22-alpine AS web
WORKDIR /app
RUN npm install -g pnpm@11.19.0
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile
COPY src ./src
COPY public ./public
COPY backend/catalog.json ./backend/catalog.json
COPY index.html tsconfig.json vite.config.ts ./
RUN pnpm build
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend ./backend
COPY --from=web /app/dist ./dist
RUN useradd -m demo && mkdir data && chown demo:demo data
USER demo
EXPOSE 8000
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
