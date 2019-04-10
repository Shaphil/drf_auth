# Django REST Framework Auth
A custom authentication system for the Django REST Framework aka DRF. This is built around a custom User model. It exposes the following routes:

```
login/
logout/
register/
reset/create/
reset/activate/<str:token>/
```

---
Follow these steps to run the app locally:

 - Clone the repository
 - `cd drf_auth`
 - `virtualenv env`
 - `source env/bin/activate`
 - `pip install -r requirements.txt`
 - Open up `settings.py` and set proper values for `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`
 - `cd api`
 - `./manage.py runserver`
 
---
- Now create a user from the `register/` endpoint. `register/` expects a `username`, `email` and a `password`. 
```
{
  POST  register/
  
  "username": "username",
  "email": "id@e.mail",
  "password": "password"
}
```
- To reset password make a post request with the registered `username` to `reset/create/`. You should get an activation link in your `email`. 
```
{
  POST  reset/create/
  
  "username": "username"
}
```
- Make a post request with the new `password` to `reset/activate/<str:token>/`. Now try to login with your new `password`.
```
{
  POST  reset/activate/<str:token>/
  
  "password": "password"
}
```
