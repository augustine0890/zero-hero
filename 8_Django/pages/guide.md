# Pages App
```
mkdir pages && cd pages
pipenv install django==3.0
pipenv shell
django-admin startproject pages_project .
python manage.py startapp pages
```

`python manage.py runserver`

- Create a directory called `templates`
`mkdir templates`
`touch templates/home.html`

**Tests**
- `python manage.py test`
