# E-learing Project

## Setting up
```
mkdir env
python3 -m venv env/educa
source env/educa/bin/activate
```

- Install Django
    - `pip install Django==3.0`
- Manage image uploads
    - `pip install Pillow==7.0.0`
- Create a new project
    - `django-admin startproject educa .`
- Create a new application
    - `django-admin startapp courses`

## Build the Models
- Create the initial migration for application
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- Dump out the data from model database
    - `python manage.py dumpdata courses --indent=2`
    - `python manage.py dumpdata --help`

**Using fixtures to provide initial data for models**
```
mkdir courses/fixtures
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/
subjects.json
```
- Load the fixture into the database
    - `python manage.py loaddata subjects.json`

## Model Inheritance
- __Abstract models__: useful when you want to put some common information into several models.
- __Multi-table model inheritance__: applicable when each model in the hierarchy is considered a complete model by itself
- __Proxy models__: useful when you need to change the behavior of a model.

## Custom model fields
- Writing custom model fields at [link](https://docs.djangoproject.com/en/3.1/howto/custom-model-fields/)

## Authentication templates
- `http://127.0.0.1:8000/accounts/login/`

## Using mixins for class-based views
- Class- based views [Link](https://docs.djangoproject.com/en/3.1/topics/class-based-views/mixins/)
- Multiple optional features for a class
- Particular feature in several classes

## Using mixins from django-braces
- Check a list of all mixins provided by `django-braces` at [here](https://django-braces.readthedocs.io/en/latest/)
- `pip install django-braces==1.14.0`
