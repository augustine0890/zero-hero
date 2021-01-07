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


## Docker
- Everyone needs to have the same set up the problem only magnifies.
- Simply share two files a _Dockerfile_ and _docker-compose.yml_ file.
- __Docker__ is a way to isolate an entire operating system via Linux containers which are a type of virtualization.

**Virtual Environments**
- Popular tools: `virtualenv`, `venv`, and `pipenv`
- They cannot isolate non-Python software like a PostgreSQL, Redis. And they still reply on a global, system-level installation of Python.

**Docker**
- Confirm version
    - `docker --version`
- Docker compose: to help automate commands
    - `sudo pip install docker-compose` (only in Linux)

**Images, Containers, and the Docker Host**
- Docker __image__ is a snapshot in time of what a project contains.
- _Dockerfile_ is literally a list of instructions that must be built.
- Docker __container__ is a running instance of an image.
- Docker host is the underlying OS. It's possible to have multiple containers running within a single Docker host. Code or processes are running in the Docker host.
- Create a `Dockerfile`
    - `PYTHONUNBUFFERED` ensures our console output looks familiar and is not buffered by Docker.
    - `PYTHONDONTWRITEBYTECODE` means Python will not try to write `.pyc` files.
    - The benefit of a lock file is that this leads to a deterministic build: no matter how many times you install the software packages, you’ll have the same result.
    - Use the `--system` flag to ensure the packages are available throughout all of Docker.
- Build the image
    - `docker build -t <name> .`. The period, `.`, indicates the current directory is where to execute the command
- Create a `docker-compose.yml`
    - `services`: (or containers) that want to running within Docker host. It's possible to have multiple `services` running.
    - The volumes mount automatically syncs the Docker filesystem with local computer's filesystem
    - Run Docker container: `docker-compose up`

## PostgreSQL
- Adding the `--build` flag to force an image build when software packages are updated
- Opposed to locally: 
    - `docker exec -it <name> <command>`
- PostgreSQL is not file-based. When execute `docker-compose down` all data within it will be lost.
- In `project/settings.py`
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432
        }
    }
    ```
**Psycopg**
- Database adapter for Python.
- Install Psycopg
    - `docker exec <name> pip install psycopg2-binary==2.8.5`
    - `pip install --upgrade pip`