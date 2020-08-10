web: gunicorn Meta_DPi_Server.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate