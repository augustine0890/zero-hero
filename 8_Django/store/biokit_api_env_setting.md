## 1. install "Github desktop"
   

## 2. Git clone [Link](https://github.com/FitpetKorea/fitpet-biokit-apiserver)
![img.png](img.png)
   "Code" -> "Open with GitHub Desktop" -> in URL Tab, local path 설정 후 "Clone"
   
## 3. "apiserver" directory 선택 후 오픈
![img_1.png](img_1.png)

## 4. install "pyenv" : python version control tool
  ```zsh
    $ sudo xcode-select --install
    $ brew install homebrew/dupes/zlib
    $ brew install pyenv
    $ vi ~/.zshrc

    # insert below text to .zshrc

    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"
    export PATH="/Applications/Postgres.app/Contents/Versions/12/bin:$PATH"

    alias l='ls -l'
    alias ll='ls -l'

    eval "$(pyenv virtualenv-init -)"

    # go back to zsh shell
    $ pyenv install --list
    $ pyenv --version
    $ pyenv install 3.8.6
    $ pyenv versions
  ```

## 5. install "pyenv-virtualenv" [Doc Link](http://taewan.kim/post/python_virtual_env/)
  ```zsh
    $ brew install pyenv-virtualenv
    $ pyenv virtualenv 3.8.6 biokit_api # biokit_api 는 가상환경 이름
    $ pyenv activate biokit_api # biokit_api 가상환경 활성화
    $ pyenv deactivate # 가상환경 비활성화
    $ pyenv versions
  ```
## 6. postgresql 설치
- PostgreSQL 설치 (not pyenv) [Link1](https://jinmay.github.io/2019/02/16/postgresql/how-to-install-psql-on-mac/)
[Link2](https://neulpeumbomin.tistory.com/9)
[Link3](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)
- psycopg2 설치 (in pyenv)
  ```zsh
  $ pip install psycopg2-binary
  ```
  if error occured, $ pip install --upgrade pip and try again
- start daemon (not pyenv)
  ```zsh
  $ pg_ctl -D /usr/local/var/postgres start
  ```
- default postgres 유저로 접속 (not pyenv)
  ```zsh
  $ psql postgres
  ```
  psql shell (not pyenv)
  ```postgresql
  /du
  ```
목록을 보면, 맥의 경우 맥 사용자 이름으로 role이 생성되어있는 것을 확인 할 수 있음

- pgadmin4 설치 [Doc Link](https://www.pgadmin.org/download/pgadmin-4-macos/)
- 서버 설정(pgadmin4)
  - 비밀번호 설정 : 편한 비밀번호 아무거나 설정, pgAdmin에 대한 비밀번호임
   - Server 등록
     - 좌측 메뉴의 Servers에 마우스 우클릭 `Create` -> `Server`
     - `General`
     - `Name`: biokit_api
     - `Connection`
     - `Host`: localhost
     - `Connection`
     - `username`: 사용자 이름, 최초 로그인시 계정은 mac 사용자 계정의 이름
     - `password`: 없음.

- role 생성
  - 설정된 서버 로그인 후 좌측 메뉴의 `Servers` -> `local`(등록한 서버 이름) -> `Login/Group Roles` -> 마우스 우클릭 
  - `Create` -> `Login/Group Role...` 선택
  - 정보 입력
    - `General`
    - `Name`: biokit_api
    - `Privileges`
    - `Can login`: `Yes`
    - `Superuser`: `Yes` => 나머진 알아서 `Yes`로 변경됨.
  - `Save` 선택

- create database 'biokit-api'

## 7. mysql 설치 후 설정
- Install mysql in global (not pyenv)
    ```zsh
    $ brew install mysql
    # after install
    $ mysql.server start
    ```
- Create mysql db and role (not pyenv)
    ```mysql
    create user ahead@localhost identified by {your password};
    grant all privileges on ahead.* to 'ahead'@'localhost' with grant option;
    ```
- Install Mysql Workbench
[Link](https://dev.mysql.com/downloads/workbench/)
- Create schema 'ahead' in Mysql Workbench

## 8. pycharm 세팅
  - preference > terminal
    - environment variables: 
    ```
    PYTHONUNBUFFERED=1;
    DJANGO_DB_NAME=biokit_api;
    DJANGO_DB_USERNAME=biokit_api;
    DJANGO_DB_PASSWORD={your postgres password};
    DJANGO_DB_HOST=127.0.0.1;
    DJANGO_DB_PORT=5432;
    DJANGO_AHEAD_DB_NAME=ahead;
    DJANGO_AHEAD_DB_USERNAME=ahead;
    DJANGO_AHEAD_DB_PASSWORD={your mysql password};
    DJANGO_AHEAD_DB_HOST=127.0.0.1;
    DJANGO_AHEAD_DB_PORT=3306;
    DJANGO_SETTINGS_MODULE=apiserver.settings
    ```

- change DJANGO_AHEAD_DB_PASSWORD field to mysql password

- setup python interpreter

## 9. Migration and run django project
  ```zsh
    # Open terminal
    # in pyenv
    # Install requirements
    $ pip install -r requirements.txt
    # makemigrations 
    $ python manage.py makemigrations
    # default DB migrate
    $ python manage.py migrate
    # ahead DB migrate
    $ python manage.py migrate --database=ahead
    # run
    $ python manage.py runserver
  ```

## 10. Commands
  ```zsh
    # psql start
    $ pg_ctl -D /usr/local/var/postgres start
    # psql stop
    $ pg_ctl -D /usr/local/var/postgres stop
    # mysql start
    $ mysql.server start
    # mysql stop
    $ mysql.server stop
  ```


