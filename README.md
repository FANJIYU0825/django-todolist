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

we add  in code in /views

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

invitation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

Examples:

Function views

    1. Add an import:  from my_app import views

    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
 
    1. Add an import:  from other_app.views import Home
 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf

    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))



and add in url /wedding
    ```
    from django.contrib import admin
    from django.urls import path
    from photo.views import myView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('photo/', myView),
    ]
    ```

type same

`python manage.py runserver`


```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```


you will see the /photo page

## fourth step

**add html in side the django**
in the django or flask we allaways need to 
add`mkdir templates` 


template folder that we add html or css inside  


now add a new apps  
`python manage.py startapp polls`


```
from django.shortcuts import render

def visiter_see(request):

    return render(request,'visiter.html')
```
if you run the server now the django won't catch the  `/template XXX.html` 

```
/wedding  setting.py

add the  dirs we need

'DIRS': [os.path.join(BASE_DIR,'templates')],
```