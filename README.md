# Тесты производительности

Нагрузочные тесты для [учебного банковского стенда](https://github.com/Nikita-Filonov/performance-qa-engineer-course). Реализованы на Python + Locust, поддерживают HTTP и gRPC.

**Стек:** Python, Locust, Pydantic, httpx, grpcio, Docker.

## Структура

- `scenarios/` — сценарии Locust (HTTP/gRPC)
- `clients/` — HTTP и gRPC клиенты
- `seeds/` — генерация тестовых данных
- `tools/` — конфигурация и утилиты

## Быстрый старт

```bash
git clone https://github.com/McSuit/performance-tests.git
cd performance-tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

```bash
locust --config=./scenarios/http/gateway/existing_user_get_documents/v1.0.conf
```

HTML-отчёт сохраняется рядом со сценарием: `scenarios/.../report.html`.

## Мониторинг

- Grafana: http://localhost:3002
- Prometheus: http://localhost:9090

## CI/CD

GitHub Actions запускает сценарии в headless-режиме и публикует отчёты на GitHub Pages. Конфиг: `.github/workflows/performance-tests.yml`.

