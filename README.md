# О приложении
    Сделал соблюдая чистую архитектуру
    Используется в качестве tron gateway -- api shasta

    src/core/container точка старта управления зависимостями
    src/tron_app/presentation - api


# ТЕСТЫ
    Реализован паттерн uow, для него написаны тесты для коммитов и откатов транзакций
    Сделал тесты юскейсов тоже
    Также сделано 2 интеграционных теста для ручек, при которых подменяется окружение
    на тестовое из .env.test плюс мокается gateway AsyncClient, для проверки работы приложения

        uv run pytest -vv

    адреса для проверки:
        TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8
        TBhC4DefkF79z1B8MBbXRjAhMsWk5r3VLf
        TLBJML1LhqRePGBQVTmWFaTYeKgNpJwjKq
        TDeeUerUt6V3nZWS7Cko3WzT1WKVTgtsLJ

# Запуск
    2 контейнера база + приложение
    запуск из корня
        docker compose up -d --build

