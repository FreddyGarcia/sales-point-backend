release: python manage.py migrate
release: python manage.py loaddata db.json
web: gunicorn SalesPoint.wsgi
