FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

RUN pip install uv

WORKDIR /src

COPY uv.lock pyproject.toml ./

RUN uv sync --frozen

COPY . .    

RUN chmod +x docker/app_entrypoint.sh

CMD ["bash", "docker/app_entrypoint.sh"]