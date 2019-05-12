# facebook login and graph api

## Requirements
- python3.7
- pip

## installation
`pip install -r requirements.txt`

## Environment variables to set
example
```
SECRET_KEY=this-is-very-secret
DATABASE_URL=valid-database-url-string  # default is sqlite.postgres drivers are alse installed
DEBUG=True
```

## run migrations
1. Django: `python manage.py migrate && python manage.py collectstatic --noinput`
2. Database's initial state: Execute queries from initial_state.sql modifying parameters as per ned


## run
`cd web && python manage.py runserver`

## unit test
`python manage.py test`


# Dockerization
1. Use Dockerfile for production. Steps:
```
1. Set SECRET_KEY, DEBUG and DATABASE_URL environment variables. Can also be done with docker run
2. Setup database
3. docker build -t <tag> .
4. docker run <tag>
```

2. Use docker-compose.yml for local development. Steps:
```
1. docker-compose up --build
2. docker exec -it <container_id> python web/manage.py createsuperuser  # this is to create a superuser
3. Follow django-allauth settings to set the website settings from django admin panel.
```
