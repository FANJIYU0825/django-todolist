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