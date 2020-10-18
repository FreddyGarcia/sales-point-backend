python manage.py flush --noinput
python manage.py makemigrations core
python manage.py migrate
python manage.py loaddata db.json