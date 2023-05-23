init:
	cp .env.example .env
	docker-compose down --volumes
	docker-compose rm -f
	docker-compose build --no-cache
	docker-compose up -d

up:
	docker-compose up

stop:
	docker-compose stop

migrate:
	docker-compose exec app python manage.py migrate

seed:
	docker-compose exec app python manage.py database_seed
