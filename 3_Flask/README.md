# Flask Series
----
- How to create and run Flask web application.

### Creating a virtual enviroment
- Create a new virtual enviroment called `env`
`python3 -m venv env`
- Activate virtual enviroment
`source env/bin/activate`

### Updating pip
`pip install --upgrade pip`
`pip list`

### Installing Flask
`pip install flask`

### Creating a Flask app
- `touch app.py`

- `__name__` is a special variable used by the Python interpreter to understand if a file is the main program.

### Running the Flask app
- `python3 app.py`
- Stop the app by hitting `Ctrl + c`

### Flas environment variables
- Running `export FLASK_APP=app.py` will set the `FLASK_APP` variable to `app.py`
- Running `export FLASK_ENV=development` tells Flask we want to run our app in development mode
- Warning: never run a live Flask application in production using development mode
- `flask run`
- To deactivate your virtual environment: `deactivate`