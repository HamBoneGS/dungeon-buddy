FROM public.ecr.aws/docker/library/python:3.9.13-slim-bullseye as base

EXPOSE 8000

RUN apt update && apt install gcc libpq-dev -y

ENV DJANGO_SETTINGS_MODULE=dungeonbuddy.settings
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8000 --workers=4 --chdir=/app"

WORKDIR /app

COPY requirements.txt manage.py /app/
RUN pip install -r requirements.txt

COPY ./dungeonbuddy /app/dungeonbuddy
COPY ./notes /app/notes

FROM base as devserver
COPY pyproject.toml .flake8 /app/
COPY requirements-dev.txt /app/
RUN pip install -r requirements-dev.txt
CMD ["gunicorn", "dungeonbuddy.wsgi", "--reload", "--timeout=0"]

FROM base as production
# Increase keep-alive because container will be deployed behind load balancer
CMD ["gunicorn", "dungeonbuddy.wsgi", "--keep-alive 80"]