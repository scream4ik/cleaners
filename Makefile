.PHONY: requirements freeze syncdb run run-public makemessages compilemessages collectstatic user test

requirements:
	-@echo "### Installing requirements"
	-@pip install -r requirements.txt

freeze:
	-@echo "### Freezing python packages to requirements.txt"
	-@pip freeze > requirements.txt

syncdb:
	-@echo "### Creating database tables and loading fixtures"
	@python manage.py makemigrations
	@python manage.py migrate

run:
	@python manage.py runserver

run-public:
	@python manage.py runserver 0.0.0.0:8000

makemessages:
	-@python manage.py makemessages --all
	-@python manage.py makemessages -d djangojs

compilemessages:
	-@python manage.py compilemessages

collectstatic:
	@python manage.py collectstatic --noinput

user:
	-@python manage.py createsuperuser

test:
	-@python manage.py test
