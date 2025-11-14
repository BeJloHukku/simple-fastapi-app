# FastAPI + MySQL + Apache Application

Приложение для управления пользователями с FastAPI, MySQL и Apache.

## **Требования**

- Docker
- Docker Compose

## **Быстрый старт**

### **Вариант 1: Использование готовых образов**
```bash
curl -O https://raw.githubusercontent.com/BeJloHukku/simple-fastapi-app/main/docker-compose.prod.yml

docker-compose -f docker-compose.prod.yml up -d
```

### **Вариант 2: Сборка из исходников (для разработки)**
```bash
git clone https://github.com/BeJloHukku/simple-fastapi-app.git
cd app-apache

docker-compose up -d --build
```

Это создаст и запустит 3 контейнера:
- **MySQL** - база данных
- **FastAPI** - API сервер
- **Apache** - веб-сервер (прокси)

### **3. Проверьте статус**
```bash
docker-compose ps
```

## **Использование API**

### **Получить всех пользователей**
```bash
curl http://localhost/users
```

### **Получить пользователя по ID**
```bash
curl http://localhost/users/1
```

### **Проверка здоровья приложения**
```bash
curl http://localhost/health
```

## **Создание пользователей**
### **Способ 1: Через готовый Python скрипт**
```bash
docker exec app-apache-fastapi-1 python add_user.py "Igor" "igor@example.com"
```

### **Способ 2: Через curl**
```bash
curl -X POST http://localhost/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Igor","email":"igor@example.com"}'
```

## **Структура проекта**

```
app-apache/
├── fastapi/
│   ├── main.py              # Основное приложение FastAPI
│   ├── database.py          # Конфигурация БД
│   ├── models.py            # ORM модели
│   ├── db_functions.py      # Функции для работы с БД
│   ├── requirements.txt     # Python зависимости
    ├── add_user.py          # Скрипт для добавления пользователей
│   └── Dockerfile           # Dockerfile для FastAPI
├── apache/
│   ├── Dockerfile           # Dockerfile для Apache
│   └── my-httpd.conf        # Конфиг Apache
├── docker-compose.prod.yml  # Compose конфиг для использования
└── docker-compose.yml       # Compose конфиг для разработки          
```

## **Стоп приложения**

```bash
docker-compose down
```

## **Очистка (удалить все данные БД)**

```bash
docker-compose down -v
```

## **Логи**

```bash
# Логи FastAPI
docker-compose logs fastapi

# Логи MySQL
docker-compose logs mysql

# Логи Apache
docker-compose logs apache

# Все логи в реальном времени
docker-compose logs -f
```

## **Переменные окружения**

Можно изменить в `docker-compose.yml`:
- `MYSQL_ROOT_PASSWORD` - пароль MySQL root
- `MYSQL_DATABASE` - имя базы данных
- `PYTHONUNBUFFERED` - вывод логов Python в реальном времени

## **Автор**

BeJloHukku