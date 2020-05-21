# setting django 

## first step(use by env)

open terminal


`cd {the filepath} `


when the to file path typing


`pipenv shell`


open env infile typing
`pip  install django`


**if you already install just pass**

## second step (start project)
add new project in


`django-admin startproject {pj_name}`

`ls pr_name`
then you will see

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```


you if you typing
`python manage.py runserver`


```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## thir step(start an app )

**one project can have many app**
`python manage.py startapp polls`

That’ll create a directory polls, which is laid out like this:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

```




#
