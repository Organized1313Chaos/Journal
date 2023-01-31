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
## `admin.py`    
- After creating the model make sure you register in the app/admin.py
- You cannot add two different views for the same model in `admin.py`
- readonly fields to display not-editable fields `(editable=False)`

## `settings.py`
- `INSTALLED_APPS - ['appName1', 'appName2']`
- `TIME_ZONE = 'Asia/Kolkata'`
  - automatically make changes to the datetime feilds in different models

