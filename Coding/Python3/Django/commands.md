**Installation**
- ```pip -m install django```
  
**Check Django Version**
- ```python -m django --version```

**List Django Core Comands**
- ```django-admin```

**Django start project**
- ```django-admin startproject <project_name>```
<br>Note:  <br>- Change in outermost directory ```<project_name>``` is possible, innermost is depricated<br>- ```__init__.py``` file is compulsory for any python package to work<br>- ```wsgi.py``` refers to Web Server Gateway Interface

**Run project**
- ```python manage.py runserver```

**Start App**
- `python manage.py startapp <app_name>`
- `add app name in settings.py >> INSTALLED_APPS`

**migration**
- `python manage.py makemigrations <app_name>`
- `python manage.py migrate <app_name>`
  
**Create Superuser**
- `python manage.py createsuperuser`
  - `Note: Before creating supersuper you must run migration commands at least once.`


## `models.py`
- The class below is inherited in model class, such class doesn't create actual objects, instead are used for the creation of other models
    ```
    class Meta:
        # If the instance needs to be created or not
        abstract = True 

        # table_names in django_admin_panel
        verbose_name = "State"
        verbose_name_plural = "States"

        # external db table mapping
        db_table = 'State'

        #define ordering
        ordering = ['-created_at',]

        #Specific user-defined function
        import secrets
        def save(self, *args, **kwargs):
          if not self.track_id:
              alphabet = string.ascii_letters + string.digits
              self.track_id = ''.join(secrets.choice(alphabet) for i in range(10))
          super(PCCUserPackageMap, self).save(*args, **kwargs)
    ```
- Object Name to be displayed
  ```
    # Object Name to be displayed in django-admin panel
    def __str__(self):
        return str(self.uuid)
  ```
  - return type must be a string
  - Make sure timezone is appropriate in `settings.py`
    - `DateTimeField.auto_now --> updated_at`
    - `DateTimeField.auto_now_add --> created_at`

  - `blank= True (Front-End: not Required)`
  -  `null= True (Back-end: nulls are allowed)`
  -  `Enums`
     ```
        ACCEPTED_ID_DOCS=(
            ('AADHAAR','AADHAAR'),
            ('VOTER ID','VOTER ID'),
            ('DRIVING LICENSE','DRIVING LICENSE'),
            ('PASSPORT','PASSPORT')
          )
     ```
  - Setting file-path
    ```
    def set_selfie_path(instance, filename):
      format = str(instance.pk) + '/selfie/' + filename
      return format
    ``` 
    
  - `All types of fields`
    ```
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application_no = models.CharField(max_length=20, null=True, blank=True)

    def set_selfie_path(instance, filename):
      format = str(instance.pk) + '/selfie/' + filename
      return format

    selfie_path = models.FileField(upload_to=set_selfie_path, null=True, blank=True)

    ```

- **Django's Builtin User Model**
  ```
  # User Model Fields

  username: a unique identifier for each user, typically used as the login name.
  password: a hash of the user's password.
  first_name and last_name: the user's name.
  email: the user's email address.
  is_staff: a flag indicating whether the user has staff (administrator) privileges.
  is_active: a flag indicating whether the user's account is active.
  is_superuser: a flag indicating whether the user is a superuser with all privileges.
  date_joined: the date the user joined.
  last_login: the date the user last logged in.
  ```
  
  ```
  # Import:
  from django.contrib.auth.models import User
  ```

  ```
  # Create a new user
  user = User.objects.create_user(username='john', email='john@example.com', password='secretpassword')
  user.first_name = 'John'
  user.last_name = 'Doe'
  user.save()
  ```
  ```
  # Update a user's password
  user = User.objects.get(username='john')
  user.set_password('newsecretpassword')
  user.save()
  ```

  ```
  # Check if a user is authenticated
  def some_view(request):
      if request.user.is_authenticated:
          # Do something for authenticated users.
          ...
      else:
          # Do something for anonymous users.
          ...
  ```
  ```
  # Check if a user is a staff member
  user = User.objects.get(username='john')
  if user.is_staff:
      # Do something for staff members
      ...
  ```
- Mandatory Fields: Username, Passwords, Email; others can be left blank
- Built-in Authentication: username and password are mandatory
- Built-in password reset functionality: Email field is mandatory
## `admin.py`    
Imports:
```
from django.contrib import admin
from .models import *
```

example:
```
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.get_fields()]
```

registration:
```
admin.site.register(User, UserAdmin)
```

- After creating the model make sure you register in the app/admin.py
- You cannot add two different views for the same model in `admin.py`
- readonly fields to display not-editable fields `(editable=False)`
- `list_display = [field.name for field in Book._meta.get_fields()]`
- `NOTE:` `list_display = '__all__' doesn't work for admin-panel, works for serializer though` 

## `settings.py`
- `INSTALLED_APPS - ['appName1', 'appName2']`
- `TIME_ZONE = 'Asia/Kolkata'`
  - automatically make changes to the datetime feilds in different models

## `views.py`
Imports:
```
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
```

Examples:
```
# HttpResponse
def analyze(request):
    # get the POST request parameters
    text = request.POST.get('text', 'default')

    return HttpResponse(f'Returns response-string')
```

```
# render Response
def index(request):
    google = r"https://google.com"
    leetcode = r"https://leetcode.com/"
   
    params = {'google': google, 'leetcode': leetcode}
    #render returns a template and context dictionary
    return render(request, 'index.html', params)
```

```
class CheckTabIndex(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request,pk):   
        # var = Model.objects.get( attr = attr_val )
        docs = PCCDocument.objects.get(user_pack=pk)
        docs_s = PCCDocumentSerializer(docs)
        return Response(responsedata(True, "Data fetched successfully!", 200,data=docs_s.data),status=status.HTTP_200_OK)
```

**Pagination**
- Link: [Pagination](https://www.geeksforgeeks.org/how-to-add-pagination-in-django-project/)
- 1-based indexing 