# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10-alpine

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо залежності всередині контейнера
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME
COPY . $APP_HOME

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "virtual_assistant_v007/main.py"]
