cd src

uv run alembic revision --autogenerate

uv run alembic upgrade head

uv run uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000