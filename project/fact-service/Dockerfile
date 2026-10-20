FROM python:3.14-slim

WORKDIR /fact-service

COPY pyproject.toml poetry.lock .

RUN pip install poetry && poetry install --without dev --no-root

COPY /app .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "3"]