# Платформа онлайн-обучения <img width="137" height="41" alt="Skypro" src="https://github.com/user-attachments/assets/ac708293-d4d3-4222-980d-a89643052ae0" />

Бэкенд-часть SPA-приложения для платформы онлайн-обучения, разработанная на **Django** и **Django REST Framework**.

## Функционал проекта
* **Кастомная модель пользователя (`users.User`):**
  * Авторизация по `email` (стандартное поле `username` отключено).
  * Дополнительные поля профиля: `phone`, `city`, `avatar`.
  * Реализован эндпоинт для просмотра и редактирования профиля любого пользователя через `RetrieveUpdateAPIView` (дополнительное задание).
* **Учебные материалы (`materials`):**
  * **Курсы (`Course`):** полный CRUD реализован через `ModelViewSet` и роутер `DefaultRouter`.
  * **Уроки (`Lesson`):** полный CRUD реализован через `Generic`-классы (`CreateAPIView`, `ListAPIView`, `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`), связь с курсами «один ко многим».

## Технологический стек
* Python 3.12+
* Django
* Django REST Framework
* Pillow (работа с изображениями и медиафайлами)
* Poetry (управление зависимостями и виртуальным окружением)

## Установка и запуск проекта

1. **Клонируйте репозиторий и перейдите в директорию проекта:**
   ```bash
   # 30.1 клонируем удаленный репозиторий на локальный компьютер
   git clone <ссылка_на_ваш_репозиторий>
   cd 30-1_Django_DZ
   ```

2. **Установите зависимости через Poetry:**
   ```bash
   # 30.1 устанавливаем все зависимости проекта из файлов pyproject.toml и poetry.lock
   poetry install
   ```

3. **Примените миграции базы данных:**
   ```bash
   # 30.1 создаем таблицы в базе данных на основе миграций проекта
   poetry run python manage.py migrate
   ```

4. **Создайте суперпользователя (при необходимости):**
   ```bash
   # 30.1 создаем учетную запись администратора (логин вводится в формате email)
   poetry run python manage.py createsuperuser
   ```

5. **Запустите локальный сервер разработки:**
   ```bash
   # 30.1 запускаем тестовый веб-сервер Django
   poetry run python manage.py runserver
   ```

## Основные эндпоинты API

### Курсы (`ViewSet` + `DefaultRouter`)
* `GET /courses/` — получение списка всех курсов
* `POST /courses/` — создание нового курса
* `GET /courses/<id>/` — получение детальной информации о курсе
* `PUT / PATCH /courses/<id>/` — полное или частичное обновление курса
* `DELETE /courses/<id>/` — удаление курса

### Уроки (`Generic`-классы)
* `POST /lessons/create/` — создание нового урока
* `GET /lessons/` — получение списка всех уроков
* `GET /lessons/<id>/` — получение детальной информации об уроке
* `PUT / PATCH /lessons/update/<id>/` — полное или частичное обновление урока
* `DELETE /lessons/delete/<id>/` — удаление урока

### Пользователи (`Generic`-классы)
* `GET /users/<id>/` — просмотр профиля пользователя
* `PUT / PATCH /users/<id>/` — редактирование профиля пользователя

* Главная страница: [http://127.0.0.1:8000/](http://127.0.0)
* Административная панель Django: [http://127.0.0.1:8000/admin/](http://127.0.0admin/)

## Структура проекта

```text
30-1_Django_DZ/                     # 30.1 Корневая директория проекта (платформа онлайн-обучения на DRF)
│
├── config/                         # 30.1 Главная конфигурационная папка проекта Django
│   ├── __init__.py                 # 30.1 Инициализация пакета конфигурации проекта
│   ├── asgi.py                     # 30.1 Асинхронный интерфейс веб-сервера
│   ├── settings.py                 # 30.1 Главные настройки проекта (INSTALLED_APPS, DRF, AUTH_USER_MODEL, MEDIA)
│   ├── urls.py                     # 30.1 Главный файл маршрутизации (пути admin, приложений materials и users, медиафайлы)
│   └── wsgi.py                     # 30.1 Синхронный интерфейс веб-сервера
│
├── materials/                      # 30.1 Приложение «Учебные материалы» (Курсы и уроки)
│   ├── migrations/                 # 30.1 Папка миграций приложения в базе данных
│   │   ├── 0001_initial.py         # 30.1 Создание таблиц Course и Lesson с внешним ключом на курс
│   │   └── __init__.py             # 30.1 Инициализация пакета миграций
│   ├── __init__.py                 # 30.1 Инициализация пакета приложения materials
│   ├── admin.py                    # 30.1 Регистрация моделей Course и Lesson в панели администратора
│   ├── apps.py                     # 30.1 Конфигурация приложения materials
│   ├── models.py                   # 30.1 Модели БД: Course (название, превью, описание) и Lesson (связь с курсом, видео)
│   ├── serializers.py              # 30.1 Сериализаторы DRF (CourseSerializer и LessonSerializer) для преобразования в JSON
│   ├── tests.py                    # 30.1 Модуль для написания автотестов приложения
│   ├── urls.py                     # 30.1 Маршруты API (DefaultRouter для курсов и path для Generic-уроков)
│   └── views.py                    # 30.1 Контроллеры API: CourseViewSet (ModelViewSet) и Generic-классы для Lesson
│
├── users/                          # 30.1 Приложение «Пользователи» (Кастомная модель и профиль)
│   ├── migrations/                 # 30.1 Папка миграций пользователей в базе данных
│   │   ├── 0001_initial.py         # 30.1 Создание кастомной таблицы User с авторизацией по email
│   │   └── __init__.py             # 30.1 Инициализация пакета миграций
│   ├── __init__.py                 # 30.1 Инициализация пакета приложения users
│   ├── admin.py                    # 30.1 Регистрация кастомной модели User в административной панели Django
│   ├── apps.py                     # 30.1 Конфигурация приложения users
│   ├── models.py                   # 30.1 Кастомная модель User (без username, вход по email, поля phone, city, avatar)
│   ├── serializers.py              # 30.1 Сериализатор UserSerializer для просмотра и редактирования профиля пользователя
│   ├── tests.py                    # 30.1 Модуль для написания автотестов пользователей
│   ├── urls.py                     # 30.1 Маршруты API для просмотра и редактирования профиля пользователя по ID
│   └── views.py                    # 30.1 Контроллер API UserUpdateAPIView (RetrieveUpdateAPIView) для профиля
│
├── .gitignore                      # 30.1 Список файлов и папок, игнорируемых системой Git (venv, media, db.sqlite3, .env)
├── manage.py                       # 30.1 Главный управляющий скрипт Django-проекта
├── pyproject.toml                  # 30.1 Конфигурационный файл Poetry со списком зависимостей (Django, DRF, Pillow)
├── poetry.lock                     # 30.1 Зафиксированные версии установленных библиотек Poetry
└── README.md                       # 30.1 Документация проекта и инструкция по запуску для проверки ДЗ
```
### Основный команды
#### 30.1 инициализируем новый проект Poetry в текущей директории (если pyproject.toml еще не создан)
poetry init -n

#### 30.1 устанавливаем Django, Django REST Framework и библиотеку Pillow через Poetry
poetry add django djangorestframework pillow

#### 30.1 создаем новый Django-проект с именем config внутри виртуального окружения Poetry
poetry run django-admin startproject config .

#### 30.1 создаем приложение users для модели кастомного пользователя
poetry run python manage.py startapp users

#### 30.1 создаем приложение materials для моделей курса и урока
poetry run python manage.py startapp materials

#### 30.1 запускаем тестовый сервер Django через Poetry для проверки работоспособности проекта
poetry run python manage.py runserver

#### 30.1 генерируем файлы миграций для созданных моделей в приложениях users и materials
poetry run python manage.py makemigrations

#### 30.1 применяем все миграции и создаем таблицы в базе данных
poetry run python manage.py migrate

#### 30.2 запускаем кастомную команду для наполнения таблицы платежей тестовыми данными
poetry run python manage.py fill_payments

#### 30.2 выгружаем данные платежей напрямую в файл payments_fixture.json
poetry run python -Xutf8 manage.py dumpdata users.Payment --indent 2 -o payments_fixture.json
