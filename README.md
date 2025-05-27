# Weather Forecast Web App

Простое веб-приложение на FastAPI, которое позволяет пользователям получать прогноз погоды по названию города. 

---

## Особенности

- Ввод города с автодополнением (autocomplete)
- Получение прогноза погоды с Open-Meteo API
- Сохранение истории поиска для каждого пользователя (по cookie)
- При повторном заходе предлагает погоду в последнем просмотренном городе
- API для статистики по количеству запросов по городам

---

## Стек технологий

- Python 3.12
- FastAPI
- SQLAlchemy + SQLite
- Jinja2 для шаблонов
- JavaScript для фронтенда (fetch + datalist)
- Docker

---

## Структура проекта
<pre>
├── src/
│   ├── main.py         # Точка входа FastAPI
│   ├── routes.py       # Маршруты приложения
│   ├── models.py       # SQLAlchemy модели
│   ├── crud.py         # Функции для работы с БД
│   ├── weather.py      # Логика для получения погоды
│   ├── database.py     # Настройка БД
│   ├── static/         # Статические файлы (JS, CSS)
│   └── templates/      # HTML шаблоны Jinja2
├── tests/              # Тесты приложения
├── Dockerfile          # Dockerfile
├── requirements.txt    # Зависимости Python
└── README.md           # Этот файл
</pre>
## Быстрый старт

- Клонировать репозиторий
-  Запуск без Docker (локально)
    Установка зависимостей
    
        #Рекомендуется создать и активировать виртуальное окружение:
        
        python -m venv venv
        source venv/bin/activate   # Linux/macOS
        venv\Scripts\activate      # Windows
        
        #Установите все зависимости из requirements.txt:
        
        pip install -r requirements.txt
    
    Запуск приложения
        
        #Запустите FastAPI сервер с помощью uvicorn:
        
        uvicorn src.main:app --reload
        
    
    Открытие в браузере
    
        #Перейдите по адресу:

           http://localhost:8000
        
        #Вы увидите форму для ввода города и кнопку для получения прогноза погоды.
   
- Запуск с Docker
    Сборка Docker образа
    
        #В корне проекта выполните команду:
        
        docker build -t weather-app .
    
    Запуск контейнера
    
        docker run -d -p 8000:8000 weather-app
    
    Проверка работы
    
        #Откройте в браузере:
  
          http://localhost:8000

---
  
## Тестирование

Для запуска тестов используйте pytest:

    python -m pytest tests/

    #Тесты проверяют корректность работы API и основных функций приложения.

