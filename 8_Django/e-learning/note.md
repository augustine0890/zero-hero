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