# Dotamind AI Architecture

## Общая схема

Пользователь

↓

Frontend (Next.js)

↓

Backend API (FastAPI)

↓

Dota Data API

↓

Analyzer Engine

↓

AI Coach

↓

Отчет пользователю


---

# Backend

Backend отвечает за:

- получение матчей;
- обработку данных;
- анализ игры;
- создание рекомендаций.


Структура:

backend/

app/

main.py

api/

services/

analyzers/

models/


---

# Analyzer Engine

Модули анализа:

farm_analyzer.py

death_analyzer.py

item_analyzer.py

draft_analyzer.py

skill_analyzer.py

teamfight_analyzer.py


---

# Frontend

Frontend отвечает за:

- сайт;
- ввод Match ID;
- отображение отчета;
- аккаунт пользователя.


---

# Database

Хранит:

- пользователей;
- матчи;
- отчеты;
- настройки.


---

# Версия MVP

Первая задача:

Пользователь вводит Match ID.

Система:

1. Получает матч.
2. Анализирует данные.
3. Создает отчет.
4. Показывает результат.