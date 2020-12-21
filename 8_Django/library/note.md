# Library Website and API

## Traditional Django

**Installation**
- `mkdir library && cd library`
- `pipenv install django==3.0.3`
- `pipenv shell`
- `django-admin startproject library_project .`

```
.
├── Pipfile
├── Pipfile.lock
├── library_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── note.md
```
- Run `migrate` to sync the database with Django's default settings.<br>
`python manage.py migrate` <br>
`python manage.py runserver`

**First App**
- Create a `books` app
`python manage.py startapp books`

```
.
├── Pipfile
├── Pipfile.lock
├── books
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── library_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── note.md
```
- Create a super user account<br>
`python manage.py createsuperuser` user/pw: augustine/fitpet123

**Django REST Framework**
- `pipenv install djangorestframework==3.11.0`
- Create a new `api` app
`python manage.py startapp api`

**Serializers**
- A serializer translates data into a format that is easy to consume over the internet
    - Typically JSON
    - Display at an API endpoint