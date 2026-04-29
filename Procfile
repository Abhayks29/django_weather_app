web: gunicorn weatherproject.wsgi --log-file -
release: python manage.py migrate && python manage.py collectstatic --noinput
