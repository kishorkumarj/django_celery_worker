# Django-base-server

Start Server
python3 manage.py runserver

Run redis container on default port
docker run -itd -p 6379:6379 redis:alpine3.18

Start Celery worker
python3 -m celery -A app_server worker -l info
