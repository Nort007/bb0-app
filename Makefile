all: down build migrate fake-data

down:
	docker-compose down

build:
	docker-compose up -d --build

migrate:
	docker exec -ti app-django sh -c "python tapp/manage.py migrate"

fake-data:
	docker exec -ti app-django sh -c "cd tapp/ && python manage.py shell < fake_data_scr.py"

.PHONY: all down build migrate fake-data
