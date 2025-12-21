# Telegram Bot + Django Todo App

## Описание
Телеграм-бот для управления списком задач (ToDo List), основанный на Django API. Проект реализует CRUD-операции для задач и категорий, аутентификацию через токены, уведомления через Celery и запускается через Docker Compose.

## Функциональность

### Django API
- CRUD для задач и категорий  
- Аутентификация через TokenAuthentication  
- Фильтрация задач по пользователю  
- Использование кастомных ID (не int, не UUID)  
- Поддержка часового пояса **America/Adak**  
- Уведомления о просроченных задачах через **Celery + Redis**  
- Админ-панель для управления задачами и категориями  

### Telegram-бот
- Просмотр списка задач с категорией и датой создания  
- Добавление новых задач через диалоги (**aiogram-dialog**)  
- Валидация даты при вводе  
- Связь с Django API через REST  

### Docker
Запуск всех сервисов через `docker-compose`:
- Django (gunicorn)  
- PostgreSQL  
- Redis  
- Celery Worker  
- Celery Beat  
- Telegram-бот  

## Архитектура
- **Backend:** Django + Django REST Framework  
- **Бот:** Aiogram + Aiogram-dialog  
- **БД:** PostgreSQL  
- **Фоновые задачи:** Celery + Redis  
- **Контейнеризация:** Docker, Docker Compose  

## Требования
- Docker  
- Docker Compose  

## Установка и запуск

### 1. Клонируйте репозиторий
```
git clone <your-repo-url>
cd <repo-name>
```

### 2. Создайте файл окружения
```
cp .env.example .env
```
Заполните `.env` своими данными.

### 3. Соберите и запустите проект
```
docker-compose up --build
```

### 4. После запуска
- Django API будет доступен на: http://localhost:8000  
- Telegram-бот начнёт принимать сообщения  

## Переменные окружения

| Переменная | Описание |
|-----------|----------|
| DJANGO_SECRET_KEY | Секретный ключ Django |
| DEBUG | Режим отладки (1 или 0) |
| POSTGRES_DB | Имя БД PostgreSQL |
| POSTGRES_USER | Пользователь БД |
| POSTGRES_PASSWORD | Пароль пользователя БД |
| POSTGRES_HOST | Хост БД (для Docker — `db`) |
| REDIS_URL | URL Redis (для Celery) |
| BOT_TOKEN | Токен Telegram-бота |
| API_URL | URL Django API (для бота) |
| API_TOKEN | Токен доступа к API (для бота) |

## Трудности и решения
- **Кастомные ID:** реализованы через `hashlib.sha256` и `time.time()` для отказа от int, UUID, random  
- **Связь бота и API в Docker:** использовано сетевое имя сервиса `backend`  
- **Часовой пояс:** изменён на `America/Adak`  
- **Celery:** настроен `django-celery-beat` для периодических уведомлений  

## Структура проекта
```
.
├── backend/
│   ├── apps/
│   │   ├── todo/
│   │   ├── users/
│   │   └── common/
│   ├── config/
│   ├── Dockerfile
│   └── requirements.txt
├── bot/
│   ├── api.py
│   ├── main.py
│   ├── dialogs/
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## Автор
**Abdulla Dukuzov**
