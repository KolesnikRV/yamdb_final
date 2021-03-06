# Проект "YaMDb"
![Yamdb workflow](https://github.com/KolesnikRV/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg?branch=main)

# Описание
- Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором.
- Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
- В каждой категории есть произведения: книги, фильмы или музыка.
- Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
- Новые жанры может создавать только администратор.
- Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Доступные ресурсы:
- auth: аутентификация.
- users: пользователи.
- titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
- comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

### Документация по API (http://localhost/redoc/)

# Использованные технологии~
- Python 3.8
- Django 3.0.5
- Django Rest Framework 3.12.4
- gunicorn 20.0.4
- Docker
- docker-compose
- Nginx
- Postgres

# Инструкции по запуску
## Запуск контейнеров
- $: sudo docker-compose up -d

## Создание и выполнение миграций, сбор статики, создание суперпользователя(admin:admin):
- $: docker-compose exec web make prepare

  ### Админка доступна по адресу - http://localhost/admin

# Авторы
- https://github.com/KolesnikRV/
- https://github.com/Mastiff2005
- https://github.com/abduev