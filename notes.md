## Starting a project

Run this in your terminal:

```
django-admin startproject [your_project_name]
```

ie. Suppose your project name is "storefront"

```
django-admin startproject storefront
```
The result is that `django` will create a folder named after your project name.
Inside that, there will another directory with your project name.

```
.
└── storefront
    └── storefront
```

To avoid creating this duplicate folder, you should add a period `.` at the end, as such:

```
django-admin startproject storefront .
```

What you'll get inside the project folder will be

```
.
└── storefront
    ├── __init.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

`__init__.py`: Defines the directory as a package, just as what you would normally do when you import a class from another folder. 

`settings.py`: Settings module to define your settings.

`urls.py`: Defines what urls get used for your project.

`asgi.py`/`wsgi.py`: For web deployment. Too complicated for me to understand now.

Other files that are created:

`manage.py`: A wrapper for `django-admin`, it goes a step further by taking the settings you defined into a account.

i.e.

```
django-admin runserver
```

vs

```
python manage.py runserver
```

They do the same thing, but `manage.py` will look at your settings file but `django-admin` will not. FYI: If you run the above in your terminal, you'll go to your development site.

## Creating apps

Mosh (I paraphrase): Each Django app is just a collection of apps, each providing several functionalities.

Go into your settings module to look up the apps under `INSTALLED_APPS`. 

i.e.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

We have apps for admin, authentication etc. 

[Timestamp: 24:04]

To create an app. run the following terminal command (At this point, I created a new terminal as Mosh instructed)

```
python manage.py startapp playground
```

(Stopped at 24:04)






