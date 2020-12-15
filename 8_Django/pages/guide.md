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

**Heroku**
- `brew install heroku/brew/heroku`
- Update `Pipfile.lock`
```
[requires]
python_version = "3.7"
```
Generate the appropriate `Pipfile.lock`
`pipenv lock`

- Make a new `Procfile` file
`touch Procfile`
```
Procfile
web: gunicorn pages_project.wsgi --log-file -
```
- Install `Gunicorn` as web server
`pipenv install gunicorn==19.9.0`
- Make a one-line change to `settings.py` file
`ALLOWED_HOSTS = ['*']`

- This is a security measure to prevent HTTP Host header attacks. `*` means all domains are acceptable to keep things simple.

**Deployment**
```
heroku create <pages>
    - https://git.heroku.com/thawing-reaches-28620.git
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku master
heroku ps:scale web=1
heroku open
```
- Renaming an application
`heroku apps:rename <new-name> --app <old-name>`