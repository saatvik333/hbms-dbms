FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN pip install django
COPY . .
CMD python manage.py runserver 0.0.0.0:8000
