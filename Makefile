mypy:
	python -m mypy src/ --ignore-missing-imports

ruff:
	ruff check src

black:
	black src --check

check: mypy ruff black

style:
	black src
	isort src

hooks:
	pre-commit install -t pre-commit

configure-env:
	sudo chown -R $(whoami) .
	cp .env-example .env

build:
	sudo docker compose up -d --build --force-recreate

migrate:
	sudo docker compose exec backend python app/migrate_script.py

test:
	docker compose exec backend python -m pytest -s

requirements:
	pip install poetry
	poetry update

setup: requirements hooks configure-env build migrate check
