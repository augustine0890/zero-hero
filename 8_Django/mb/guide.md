# Message Board App

```
mkdir pages && cd mb
pipenv install django==3.0
pipenv shell
django-admin startproject mb_project .
python manage.py startapp posts
```

- Make sure the database reflects the current state of your project you'll need to run `migrate` (also `makemigrations`) each time you update a model.

**Activating models**
- Create a migrations file with the `makemigrations`. Migration files create a reference of any changes to the database models.
`python manage.py makemigrations posts`
- Build the actual database with the `migrate` which executes the instructions
`python manage.py migrate`

**Django Admin**
- Create a `superuser`
`python manage.py createsuperuser`