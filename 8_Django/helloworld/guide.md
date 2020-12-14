# Hello World App
- Initial Set Up
`mkdir helloworld && cd helloworld`
- Create new virtual environment
`pipenv install django==3.0`
`pipenv shell`
- Create new project called `helloworld_project`
`django-admin startproject hellworld_project .`

- Intall `tree` with Homebrew
`brew install tree`
`tree`
```
.
├── Pipfile
├── Pipfile.lock
├── guide.md
├── hellworld_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

- The `settings.py` file controls project's settings.
- `urls.py` tells Django which pages to build in response to a browser or URL request.
- `wsgi.py` stands for Web Server Geteway Interface
- `manage.py` used to execute various Django commands such as running the local web server or creating a new app

- Start Django
`python manage.py runserver`
`python manage.py migrate`

**Create An App**
- A single Django project contains one or more apps within it that all work together.
- For example, e-commerce site might have one app for user authentication, another app for payments, and a third app to power item listing details

- Create app named `pages`
`python manage.py startapp pages`
```
.
├── Pipfile
├── Pipfile.lock
├── db.sqlite3
├── guide.md
├── hellworld_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── pages
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

**URLs, Views, Models, Templates**
- Django request/response cycle
`URL -> View -> Model (typically) -> Template
- Django _views_ determine _what_ content is displayed on a given while _URLConfs_ determine _where_ that content is going. The _model_ contains from database and the _template_ provides _styling_ for it.

