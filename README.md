[![yamdb-final-app workflow](https://github.com/agatma/yamdb_final/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/agatma/yamdb_final/actions/workflows/main.yml)

# API_YamDB

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.
Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти).
Cредняя оценка произведения высчитывается автоматически.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Cоздан в команде из трёх человек с использованим Git в рамках учебного курса Яндекс.Практикум.

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- базы данны - SQLite3
- автоматическое развертывание проекта - Docker, docker-compose
- система управления версиями - git

## Как запустить проект:

1) Клонируйте репозитроий с проектом
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3) Выполните миграции:
```
python manage.py migrate
```
4) Cоздайте суперпользователя:
```
python manage.py createsuperuser
```
5) Запустите сервер:
```
python manage.py runserver
```
__________________________________

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация доступна по адресу http://127.0.0.1:8000/redoc/

С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей

## Алгоритм регистрации пользователей
- Пользователь отправляет запрос с параметрами *email* и *username* на */auth/email/*.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес *email* .
- Пользователь отправляет запрос с параметрами *email* и *confirmation_code* на */auth/token/*, в ответе на запрос ему приходит token (JWT-токен).

## Ресурсы API YaMDb

- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
