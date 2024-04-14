.PHONY: install migrate migrations superuser run-server update
install:
	poetry install
	
migrate:
	poetry run python -m core.manage migrate

migrations:
	poetry run python -m core.manage makemigrations

superuser:
	poetry run python -m core.manage createsuperuser

run-server:
	poetry run python -m core.manage runserver

update: install migrate ;

