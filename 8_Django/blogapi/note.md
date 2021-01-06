# Blog API

- REST is protocol used to send data back and forth between servers.
- `python manage.py createsuperuser` -> user/pw: `augustine/fitpet123`

## REST Framework
- `urls.py` file for the URL routes
- `serializers.py` file to transform the data into JSON
- `views.py` file to apply logic to each API endpoint

- Install REST framework
    - `pipenv install djangorestframework==3.11.0`

**View-Level Permissions**
- Restrict API access to authenticated users.
- Add a `permission_classes` field to each view.

**Project-Level Permissions**
- AllowAny - any user, authenticated or not, has full access.
- IsAuthenticated - only authenticated, registered users have access
- IsAdminUser - only admins/superusers have access
- IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only authenticated users have write, edit, or delete privileges

## Authentication
**Session Authentication**
- Basic flow:
    - A user enters their log in credentinals (typically username/password)
    - The server verifies the credentials are correct and generates a session object that is then stored in the database
    - The server sends the client a __session ID__-not the session object itself-which is stored as a cookie on the brower.
    - On all future requests the session ID is included as an HTTP header and, if verified by the database, the request proceeds.
    - Once a user logs out of an application, the __session ID__ is destroyed by both the client and server
    - If the user later logs in again, a new __session ID__ is generated and stored as a cookie on the client.
- It's a combination of _Basic Authentication_ and Session Authentication.

**Token Authentication**
- Token-based authentication is stateless: once a client sends the initial user creden- tials to the server, a unique token is generated and then stored by the client as either a cookie or in local storage. This token is then passed in the header of each incoming HTTP request and the server uses it to verify that a user is authenticated. The server itself does not keep a record of the user, just whether a token is valid or not.

**dj-rest-auth**
- Install: `pipenv install dj-rest-auth==1.0.4`

**django-allauth**
- `pipenv install django-allauth==0.41.0`
- Update `INSTALLED_APPS` setting
    ```
    - django.contrib.sites
    - allauth
    - allauth.account
    - allauth.socialaccount
    - dj_rest_auth.registration
    ```
-  Include `EMAIL_BACKEND` and `SITE_ID`.

- Third-party packages: `dj-rest-auth` and `django-allauth`

## Viewsets and Routers
- Traditional dj has a built-in `User` model class.
- The steps for wire up new endpoints
    - New serializer class for the model
    - New views for each endpoint
    - New URL routes for each endpoint

**Viewsets**
- The way to combine the logic for multiple related views into a single class. One viewset can replace multiple views.

**Routers**
- Routers work directly with viewsets to automatically generate URL patterns