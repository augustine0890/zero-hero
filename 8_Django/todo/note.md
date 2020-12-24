# Todo API

## Backend
```
.
├── backend
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── db.sqlite3
│   ├── manage.py
│   ├── todo_project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── todos
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
└── note.md
```
**Django REST Framework**
- Default [settings](https://www.django-rest-framework.org/api-guide/settings/)

**Serializers**
- Transform data from the models into JSON that will be outputted at URLs
- In traditional Django `views` are used to customize what data to send to the templates. In DRF views do the same thing but for our serialized data.

**CORS (Cross-Origin Resource Sharing)**
- CORS requires the server to include specific HTTP headers that allow for the client to determine if and when cross-domain requests should be allowed.
`pipenv install django-cors-headers==3.2.1`

## Frontend
- Create new React app called `frontend`<br>
`npx create-react-app frontend`
`cd frontend && npm start`

**Django REST Framework + React**
`npm install axios --save`
