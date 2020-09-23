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
