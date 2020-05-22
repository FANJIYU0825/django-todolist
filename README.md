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
```
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
