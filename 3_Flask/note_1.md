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

## Jinja template inheritance
```
app
├── app
│   ├── __init__.py
│   ├── admin_views.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── img
│   │   │   └── flask.png
│   │   └── js
│   │       └── app.js
│   ├── templates
│   │   ├── admin
│   │   │   ├── dashboard.html
│   │   │   └── templates
│   │   │       └── admin_template.html
│   │   └── public
│   │       ├── index.html
│   │       └── templates
│   │           └── public_template.html
│   └── views.py
├── requirements.txt
└── run.py
```
- Start with the Bootstrap template [here](https://getbootstrap.com/docs/4.2/getting-started/introduction/#starter-template) and get the jQuery source code [here](https://code.jquery.com/jquery-3.0.0.slim.min.js).
- Import the `bootstrap.min.css` file in the `<head>`
- Add the `{% block title %}` and `{% endblock %}` tags between the `<title> </title>` tags
- Add the `{% block main %}` and `{% endblock %}` tags between the `<main> </main>` tags
- Import the `jquery.slim.min` library
- Import the `bootstrap.bundle.min.js` library
- Import out custom JavaScript file down at the bottom just like in the last part of the series
- Finally, add the `{% block script %}` and `{% endblock %}` tags just before the closing `</body>` tag

### Child templates
- Use the  `{% extends "path/to/our/template.html" %}` syntax to import a base template
- `{% block title %}Home{% endblock %}` will set the page title
- Then fill in the blocks we declared in our base template by once again, using the `{% block something %} {% endblock %}` syntax

## Jinja template design
- Access objects in Jinja with the `{{ object }}` syntax
### Looping
```
{% for variable in iterable %}
<!-- Do something with the variable -->
{{ variable }}
{% endfor %}
```
- Enumarate an iterable using `{{ loop.index }}`
- `loop.index` starts at 1. To start enumerating at 0, use `loop.index0`
- Access class attributes using the `class.attribute` syntax
- Close any `if` conditionals with the `{% endif %}` syntax
- `|` Applies a filter. For example `{{ langs|length }}` will return 4
- `~` Converts all operands to strings and concatenates them, for example `{{ "cool" ~ "==" ~ cool }}` returns `"cool==True"`
- Be sure to close the conditional or loop with an `{% endif %}` or `{% endfor %}` respectively
- Create custom filters by registering them on our app using the @app.template_filter syntax and passing it the name of the filter we want to create.
- Define a `macro` with the following syntax:
```
{% macro macro_name(**args, **kwargs) -%}
  <!-- We then define the code we want as part of our macro -->
  <!-- We have access to any args & kwargs passed into the macro -->
  <!-- We access the args and kwargs with the familiar `{{ variable }}` syntax -->
{%- endmacro %}
```

## Working with forms
- To access form data in our route, we use `request.form`.
- The `redirect` function, amongst many other things allows us to redirect the client to different parts our app.
- We could use the `required` attribute in the HTML form and let the browser do the validation for us

## Generating dynamic URLs
- to catch a a value in the URL and store it as a variable it must look `<like_this>` and follow a trailing slash.

**app/app/views.py**
```python
@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):

    print(f"foo is {foo}")
    print(f"bar is {bar}")
    print(f"baz is {baz}")


    return f"foo is {foo}, bar is {bar}, baz is {baz}"
```

## Working with JSON data
**Postman URL**
- Create a new `POST` request to URL: `http://127.0.0.1:5000/json`

**Postman body**
```yaml
{
    "name": "Julian",
    "message": "Posting JSON data to Flask!"
}
```
**cURL request**
`curl --header "Content-Type: application/json" --request POST --data '{"name":"Augustine","message":"Posting JSON data to Flask!"}' http://127.0.0.1:5000/json`
- Useful functions and methods such as `is_json`, `get_json()` and `jsonify()`, along with helpful functions such as `make_response()`.