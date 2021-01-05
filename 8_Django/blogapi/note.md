# Blog API

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