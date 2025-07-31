FROM python:3.11-slim

WORKDIR /app

#files
COPY app/ ./app/
COPY .env ./
COPY requirements.txt ./

#dependencies
RUN pip install --no-cache-dir -r requirements.txt

#port
EXPOSE 8080

#Flask app
CMD ["python", "app/app.py"]
