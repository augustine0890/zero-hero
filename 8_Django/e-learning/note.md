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

## CreateView
- Provides the functionality for creating model objects.
    - `template_name`: the path of the template to render this view.
    - `form_class`: the form for creating objects, which has to be _ModelForm_.
    - `success_url`: the URL to redirect the user to when the form is successfully submitted.
- The `form_valid()` method is executed when valid form has been posted. It has to return an HTTP response.

## Using the cache framework
- By caching queries, calculation results, or rendered content in an HTTP request --> avoid expensive operations
- Django's cache system at [here](https://docs.djangoproject.com/en/3.1/topics/cache/)
- Istall `Memcached`
    - `brew install memcached`
- Start `memcached`
    - `memcached -l 127.0.0.1:11211` --> `brew services start memcached`
    - Run on port `11211` by default
    - Custom host and port by using the `-l` option
    - `brew services restart memcached`
    - `brew services stop memcached`
- Python bindings
    - `pip install python-memcached==1.59`

## Cache Settings
- `CACHES`: a dictionary containing all available caches
- `CACHE_MIDDLEWARE_ALIAS`: the cache alias to use for storage
- `CACHE_MIDDLEWARE_KEY_PREFIX`: prefix to use for cache keys (Set a prefix to avoid key collisions if you share the same cache between several sites)
- `CACHE_MIDDLEWARE_SECONDS`: the default number of seconds to cache pages
BACKEND: The cache backend to use.
- `KEY_FUNCTION`: A string containing a dotted path to a callable that takes
a prefix, version, and key as arguments and returns a final cache key.
- `KEY_PREFIX`: A string prefix for all cache keys, to avoid collisions.
- `LOCATION`: The location of the cache. Depending on the cache backend, this might be a directory, a host and port, or a name for the in-memory backend.
- `OPTIONS`: Any additional parameters to be passed to the cache backend.
- `TIMEOUT`: The default timeout, in seconds, for storing the cache keys. It is 300 seconds by default, which is five minutes. If set to None, cache keys will not expire.
- `VERSION`: The default version number for the cache keys. Useful for cache versioning.

**Monitoring Memcached**
- `pip install django-memcache-status==2.2`

**Cache levels**
- __Low-level cache API__: Provides the highest granularity. Allows you to cache specific queries or calculations.
- __Template cache__: Allows you to cache template fragments.
- __Per-view cache__: Provides caching for individual views.
- __Per-site cache__: The highest-level cache. It caches your entire site.
