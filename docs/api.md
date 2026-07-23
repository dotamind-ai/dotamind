# Dotamind API Documentation

Версия:

0.0.1

---

# Анализ матча

## Endpoint

POST

/analyze-match


---

## Назначение

Получить анализ матча Dota 2 по Match ID.

---

# Request

Пользователь отправляет:

```json
{
  "match_id": 123456789
}