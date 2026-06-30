FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy requirements first to leverage Docker build cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}