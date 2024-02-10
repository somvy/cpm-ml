FROM python:3.11.5-slim-bookworm

ENV PATH=/root/.local/bin:$PATH
RUN apt-get update && apt-get install gcc curl -y && curl -sSL https://install.python-poetry.org | python3 -

# копируем файлик с зависимостями
COPY pyproject.toml poetry.lock ./

# устанавливаем либы
RUN poetry install

# копируем все остальное
COPY . .

EXPOSE 8000

CMD poetry run uvicorn main:app --host 0.0.0.0