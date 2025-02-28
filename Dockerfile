FROM python:3.11

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt alembic.ini ./

RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

COPY migrations/ migrations/
COPY src/ src/

CMD alembic upgrade head & python src/main.py | tee /app/logs/tg-bot.log
