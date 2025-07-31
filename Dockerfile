FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY .env .  # Only if your app depends on it at runtime

EXPOSE 8080

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_PORT=8080

CMD ["python", "app/app.py"]
