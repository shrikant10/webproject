## Web Project In Django

#### Installing Django

```commandline
pip install django
```

#### Starting a Django Project
```commandline
django-admin startproject webproject
```
```commandline
django-admin startproject mysite .
```
It will create a repository webproject. If we add a .(dot) at the end it will create the project in the current repo.


#### Running a server

```commandline
python manage.py runserver
```

#### Creating a reusable app

```commandline
python manage.py startapp main
```

#### File Structure of Project
```
webproject
├───manage.py
├───webproject
│        settings.py
│        urls.py
│        wsgi.py
│        __init__.py
└───requirements.txt
```

 
> __manage.py__ is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

> __settings.py__ file contains the configuration of your website.

> __urls.py__ file contains a list of patterns used by url resolver.

