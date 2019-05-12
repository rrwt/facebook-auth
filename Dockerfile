FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR code
COPY . .

EXPOSE 8000

# services like gunicorn/uwsgi can be used for this in production
# e.g. CMD gunicorn --config gunicorn_config.py config.wsgi:application
# where gunicorn_config.py is the config file for gunicorn
CMD web/manage.py runserver
