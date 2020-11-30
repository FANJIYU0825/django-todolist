# 後記 
這是我 follow CSDOJO的影片<br>
[Django 系列](https://www.youtube.com/watch?v=UyQn0BhVqNU&list=PLVAVnrCH1BlFuxZARkBbN8KXSjxPgl7Ml)

也是我第一次 使用 gitcommit 練習 <br>
也是第一次練習寫MD file 
我這邊是再補一個後記<br>
目前寫了很多篇  每天都寫 技術已經不一樣了TT
我會花些時間提高這一篇的可閱讀性<br>
回頭看看自己是多麼不太會寫文章

# setting django 

## branch know
Here is my branch

| branch name    |    hint    |  mistake|
| :---       | :----:     | :----:|
| master     | first push | env problem |
| photo_app  | new_app    | the path setting   |
| template   | html view  |class set |
| db_add     | db install |  db conmand learn|    

**Is my first time to learn the branch 
and know why the brnach is importent**

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


## step five 

add the db for django

typing
`python manage.py makemigrations`

in terminal you will get
```
Migrations for 'visiter':
visiter\migrations\0001_initial.py
 - Create model visiterItem
```

type
`python manage.py migrate`


 this conmand is to tell db  to create table
```
Running migrations:
  Applying sessions.0001_initial... OK
  Applying visiter.0001_initial... OK
```

typing
`python manage.py shell`


you will get in the shell
`>>> is the thing you need to typing`
``` python =
>>>from visiter.models import {classname}
>>> {classname}
<class 'visiter.models.visiterItem'>
    
>>> {classname}.objects.all()
not guery data yet nothing in db
<QuerySet []>

>>>a = xxx(content = 'perment todo item A')
>>> a 
<xxxItem object (None)>
>>>a.save()
```
## step six

**we add buttom  html**
```
<!---out_zone reuqest--->
<form action="/addvisiter/" method="POST">{% csrf_token %}

    <input type="text" name="content"/>
    <input type="submit" value="Add">
</form>
```
add  def() `app/views.py`
```
def addvisiter (request):
    new_item = visiterItem (content = request.POST['content'])
    new_item.save()
    return HttpResponsePermanentRedirect('/visiter/')
```
add urlpatterns `project/url.py`
```
urlpatterns = [....
path('addvisiter/',addvisiter)]
```

**we delete buttom  html**

add in for loop of item 
```
<ul>
    {% for todo_item in all_items %}
    
    <li>{{ todo_item.content }}
      <!--we will add delete butttom here--->

    </li>
    {% endfor %}
</ul>
```

add delete form here

```
        <form action="/deletevisiter/{{todo_item.id}}" method="POST">{% csrf_token %}
            <input type="submit" value="Delete"/>  
        </form>
```

add  a def() `app/views.py` 
``` python=
def deletevisiter (request,todo_id):
    item_delete = visiterItem.objects.get(id = todo_id)
    item_delete.delete()
    return HttpResponsePermanentRedirect('/visiter/')
```

add in urlpatterns `project/url.py`
```
urlpatterns = [....
path('deletevisiter/',deletevisiter)]
```

run the server and we see the db in html
`python manage.py runserver`
http://127.0.0.1:8000/visiter/
