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
