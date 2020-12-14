# Django

- Upgrade pip
`pip install --upgrade pip`
- Virtual Environments
`pip install pipenv`

- Intall Django
`mkdir django && cd django`
`pipenv install django==3.0`
- Activate the virtualenv
`pipenv shell`

- Create new Django project called `test_project`
`django-admin startproject test_projects .` --> install in the current directory-the result is instead this:
```
├── manage.py
└── test_project
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

- Running Django's local web server
`python manage.py runserver`
- Stop local server
`Control+c`
- Exit virtual enviroment
`exit`