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
`/app/models.visiterItem`
```
>>>from visiter.models import visiterItem
>>> visiterItem
<class 'visiter.models.visiterItem'>
    
>>> visiterItem.objects.all()
not guery data yet nothing in db
<QuerySet []>

>>>a = visiterItem(content = 'perment todo item A')
>>> a 
<xxxItem object (None)>
>>>a.save()
>>>b = visiterItem(content = 'perment todo item B')
>>> b 
<xxxItem object (None)>
>>>b.save()

>>> visiterItem.objects.all()
<QuerySet [<visiterItem: visiterItem object (1)>]>
```

try to add verable of all_visiterItems
```
>>>all_visiterItems = visiterItem.objects.all()

```
content
```
>>> all_visiterItems[0].content
'perment todo item A'
```

id get
```
>>> visiterItem.objects.get(id=1)
<visiterItem: visiterItem object (1)>
>>> temp =visiterItem.objects.get(id=1)
>>> temp.content
'perment todo item A'
```

we go to visiter/views.py 
add this
```
from .models import visiterItem

def visiter_see(request):
     #
    all_todo_items = visiterItem.objects.all()
    return render(request,'visiter.html',
    #let items can call items we need
    {'all_items':all_todo_items}
    )
```
add to templates jinja language
```
<ul>
    {% for todo_item in all_items %}
    <li>{{ todo_item.content }}</li>
    {% endfor %}
</ul>
```
run the server and we see the db in html
`python manage.py runserver`
http://127.0.0.1:8000/visiter/
