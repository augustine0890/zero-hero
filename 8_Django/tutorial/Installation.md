## Specifying Python Version
- First, check what versions of Python you have available
    - `pyenv versions`
    - `ls ~/.pyenv/versions/` --> Remove them all (example: `rm -rf ls ~/.pyenv/versions/biokit_api`)
- Some helpful commands
    - By default, you are still using your system Python: `python -V`
    - `which python`
    - `pyenv which python` --> actual path
- If you want to use version 3.8 --> use the `global` command
    - `pyenv global 3.8`
- Install a specific version of Python
    - `pyenv install 3.8.6`
    - `pyenv versions` --> displays all currently installed Python versions
- From left to right. The options that `pyenv` can find is the option it will use
    - `System Python -> pyenv global -> pyenv local -> pyenv shell`

## Virtual Environments and `pyenv`
- __pyenv__ manages multiple versions of Python itself.
- __virtualenv/venv__ manages virtual environments for a specific Python version.
- __pyenv-virtualenv__ manages virtual environments for across varying versions of Python.

**Creating Virtual Environments**
- Creating with a command
    - `pyenv virtualenv <python_version> <environment_name>`
    - `pyenv virtualenv 3.8.6 biokit-api`
- Activate/deactivate your Python versions
    - `pyenv activate <enviroment_name>`
    - `pyenv deactivate`

## Setting up `fitpet-biokit-apiserver` environment
- Git clone the project
    - `git clone https://github.com/FitpetKorea/fitpet-biokit-apiserver` --> master branch Or augustine/dev (MacOS)
- Upgrade pip
    - `pip install --upgrade pip`
- Install requirements (only MacOS)
    - `pip install -r requirements-local.txt`
    - `pip install psycopg2-binary` --> Optional if the `requiremntes.txt` doesn't have this package.
- Install PostgreSQL via homebrew
    - This [link](https://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/)
    - Install `pgAdmin4` [here](https://www.pgadmin.org/download/pgadmin-4-macos/)
    - Start/Stop Postgres Server:
        - Start manually: `pg_ctl -D /usr/local/var/postgres start`
        - Stop muanually: `pg_ctl -D /usr/local/var/postgres stop`
        - Start and stop automatically:
            - `brew services list`
            - `brew services start postgresql`
            - `brew services stop postgresql`

- Create the user and database in Postgres
    - For example: user/database <--> biokit/biokitdb
    - The reference [here](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)
- Install MySQL via homebrew
    - This [link](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)
    - Start/Stop MySQL Server:
        - Start: `mysql.server start`
        - Stop: `mysql.server stop`
        - Restart: `mysql.server restart`
    - Install the `MySQL Workbench`
- Create the user and database/schema in MySQL
    - For example: user/database <--> ahead/aheaddb
    - Create [USER](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
    - Create [DATABASE](https://matomo.org/faq/how-to-install/faq_23484/)

- Check and edit the `.evn` file:
    - Structure:
    
        | Engine      | Django Backend                                | URL                                              |
        |-------------|-----------------------------------------------|--------------------------------------------------|
        | PostgreSQL  | ``django.db.backends.postgresql``             | ``postgres://USER:PASSWORD@HOST:PORT/NAME``      |
        | MySQL       | ``django.db.backends.mysql``                  | ``mysql://USER:PASSWORD@HOST:PORT/NAME``         |
    
    - Example:
        ```
        DATABASE_URL=psql://biokit:Fitpet123@@@127.0.0.1:5432/biokitdb
        AHEAD_URL=mysql://ahead:Fitpet123@@@127.0.0.1:3306/ahead
        ```

- Run Django Project and Migrate
    - Run project: `python manage.py runserver`
    - Make migrations: 
        - `python manage.py makemigrations`
        - `python manage.py migrate`
        - `python manage.py migrate --database=ahead`
