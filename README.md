# Kekusland

Kekusland - публичное API c открытым исходным кодом, где каждый желающий может развернуть его, использовать или изменять репозиторий!
Цель проекта: Создать первое публичное API, для пополнения профиля в GitHub, но и применения новых знаний в действии.

*Requirements*
Зависимости проекта управляются с помощью Poetry, чтобы их установить, нужно скачать Poetry и загрузить зависимости.
_Установка Poetry:_ pip install poetry
_Установка зависимостей:_ poetry install
_Python 3.14_

*Структура проекта:*
project/
├── database/
│   └── init.sql
├── fact-service/
│   ├── app/
│   │   ├── api/
│   │   │   ├── router_admin.py
│   │   │   └── router_fact.py
│   │   ├── model/
│   │   │   ├── cats.py
│   │   │   └── new_fact.py
│   │   ├── yaml/
│   │   │   └── config.yml
│   │   ├── db.py
│   │   ├── exception.py
│   │   ├── main.py
│   │   └── util.py
│   ├── Dockerfile
│   ├── poetry.lock
│   └── pyproject.toml
├── docker-compose.yml
├── LICENSE
└── README.md