FROM python:latest

WORKDIR /app

COPY code /app
COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y \
    && apt-get install vim -y \
    && pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.main
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
