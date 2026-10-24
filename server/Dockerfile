# Build the React client first, then serve it through Django in the final image.
FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
COPY --from=frontend-build /app/frontend/build ./frontend/build
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 3 djangoproj.wsgi:application"]
