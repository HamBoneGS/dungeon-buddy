REPO_NAME=$(shell basename $(CURDIR))
DOCKER_EXEC=docker exec -it dungeonbuddy-web
DOCKER_RUN=docker run -it -v $(shell pwd)/dungeonbuddy:/app/dungeonbuddy $(REPO_NAME) bash -c

format:
	$(DOCKER_RUN) "black /app/dungeonbuddy"

lint:
	$(DOCKER_RUN) flake8 /app/dungeonbuddy

test:
	docker compose -f docker-compose.yml -f .docker/test.yml run --rm dungeonbuddy
	@docker stop dungeonbuddy-db-test > /dev/null || true
	@docker rm dungeonbuddy-db-test > /dev/null || true

make-migrations:
	$(DOCKER_EXEC) python manage.py makemigrations

migrate:
	$(DOCKER_EXEC) python manage.py migrate

start-jobs:
	$(DOCKER_EXEC) python manage.py startjobs

init:
	$(DOCKER_EXEC) python manage.py collectstatic --noinput
	$(DOCKER_EXEC) python manage.py migrate
	$(DOCKER_EXEC) python manage.py createsuperuser --noinput

build:
	docker compose build

up:
	docker stop dungeonbuddy-web dungeonbuddy-db || true
	docker compose up --remove-orphans

down:
	docker compose down

shell:
	$(DOCKER_EXEC) python

bash:
	$(DOCKER_EXEC) bash

clean:
	docker compose rm