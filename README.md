# Kekusland

Kekusland - публичное API c открытым исходным кодом, где каждый желающий может развернуть его, использовать или изменять репозиторий!
Цель проекта: Создать первое публичное API, для пополнения профиля в GitHub, но и применения новых знаний в действии.

*Requirements*
- Зависимости проекта управляются с помощью Poetry, чтобы их установить, нужно скачать Poetry и загрузить зависимости.
_Установка Poetry:_
```Python
pip install poetry
```
_Установка зависимостей:_
```Python 
poetry install
```
_Python 3.14_

*Структура проекта:*
```Structure
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
```

*ВАЖНОЕ НАПОМИНАНИЕ*
- Данный репозиторий является учебным и открытым, все данные в конфигурациях ложные и не используются в production. МЕНЯЙТЕ ВСЁ, ЕСЛИ ЗАХОТИТЕ ЕГО ПОДНЯТЬ НА СЕРВЕРЕ.
