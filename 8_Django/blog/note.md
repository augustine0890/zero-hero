# [Blog App Project with Django](https://augustine-blog-dj.herokuapp.com/?target=_blank)

## Blog App

**Static Files**
- Static files: CSS, JS, and images
- In a production-ready, static files would typically store on Content Delivery Network (CDN) for better performance.

**Posts**
- The posts URL: 
    - `posts/`
    - `/`

## Users App (Authentication and Authorizatioin)
- Flow: `Signup -> Login -> Homepage`

**Sign Up**
- Signup URL: `users/signup/`
- Login URL: `users/login/`
    - By default Django will look within a templates directory called `registration` for a file called `login.html` for a log in form.
    - [LoginView](https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LoginView)

**Custom User Model**
-  The official documentation [example](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example)
- Update `settings.py`
- Create a new `CustomUser` model

- Create new forms for `UserCreationForm` and `UserChangeForm`
`touch users/forms.py`

- Update `users/admin.py`
    - Delete `blog/migrations` and `db.sqlite3`
    - `python manage.py makemigrations users`
    - `python manage.py migrate`
    - `python manage.py createsuperuser` -> user/pw: `fitpet1/fitpet123@@`

Reference: [Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)

**Bootstrap**
- The [starter template](https://getbootstrap.com/docs/4.1/getting-started/introduction/) that includes the basic files needed
- Install package `django-crispy-forms`
`pipenv install django-crispy-forms==1.8.1`

**Password Change and Reset**
- "Log In" and then navigate to "Change password"
- Password change URL: 
    - `users/password_change/`
    - `users/password_change/done/`
- Password reset URL: 
    - `users/password_reset/`
    - `users/password_reset/done/`

**Permissions and Authorization**
- If you create a new post (article) and then go into the "All Posts" you will see it automatically set to the current logged-in user.
- Restrict view access to only logged in users.
- Restrict any logged in user can make changes to any post. Allow only the author of a post has this permission.

Reference: [UserPassesTestMixin](https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin)

## Deployment
**Heroku Config**
- Update `Pipfile.lock`
`pipenv lock`
- New `Procfile`
`touch Procfile`
- Install `Gunicorn`
`pipenv install gunicorn==19.9.0`
- Update `settings.py`
`ALLOWED_HOSTS = ['*']`

**Deployment**
- `heroku git:remote -a augustine-blog-dj`
- `git push heroku master`