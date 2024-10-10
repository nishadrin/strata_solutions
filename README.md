# Strata blog



[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


## Запуск
### Поднимаем контейнер
```docker-compose -f docker-compose.local.yml up -d```
### Создаем суперпользователя
```docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser```
### Пользуемся
