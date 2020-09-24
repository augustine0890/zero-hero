## Flask application structure
- By far the most popular way to structure your application is by using the package method, where we define our Flask application as a package and can import it! Just like we would any other Python package.
- Inside `app` project directory:
```
.
├── app
│   ├── __init__.py
│   └── views.py
├── env
├── requirements.txt
└── run.py
```

- Think of the `__init__.py` file as a contructor that pulls all of the parts of our application together into a package and then tells Python to treat it as a package!

### Requirements
- From the root `app` directory, run the following:
`pip freeze > requirements.txt`
- To install packages from a `requirements.txt` file, run `pip install -r requirements.txt`

## Serving HTML files
- Move into the `app` directory with: `cd app`
- Create the `templates` directory and move into it: `mkdir templates` `cd templates`
- Create a template called `index.html`
`touch index.html`

- The project file structure should now look like the following:
```
.
├── app
│   ├── __init__.py
│   ├── admin_views.py
│   ├── templates
│   │   └── index.html
│   └── views.py
├── requirements.txt
└── run.py
```
- Flask will look in the `templates` directory we've just created for `index.html` (It's the default place Flask will go to look for HTML files when the `render_template` function is called)

### Template directories
- We're going to create 2 new directories within our `templates` directory:
    - public - will contain all of the HTML files we want to serve from `views.py`
    - admin - will contain any HTML files we'll serve from our admin routes in `admin_views.py`

## Serving static files
```
├── app
│   ├── __init__.py
│   ├── admin_views.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── img
│   │   │   └── my-image.png
│   │   └── js
│   │       └── app.js
│   ├── templates
│   │   ├── admin
│   │   │   └── dashboard.html
│   │   └── public
│   │       └── index.html
│   └── views.py
├── requirements.txt
└── run.py
```
- Flask has a function called `url_for` which can be used in our HTML to provide a path to any static files we want to fetch.
