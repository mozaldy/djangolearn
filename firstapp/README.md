# Django Tutorial
## 1. Prerequisite
- Install Django

    ```sh
    pip install django
- Create new project

    ```sh
    django-admin startproject PROJECTNAME
- Test run
    ```sh
    cd PROJECTNAME
    python manage.py runserver
- To add new app inside project
    ```sh
    python manage.py startapp APPNAME
## 2. New App
- Create function in `views.py`  
- Create `urls.py` and add url using `path()` function inside `urlpatterns[]` to connect http request to the views made previously
## 3. Root App
- in `settings.py` add the new app to `INSTALLED_APPS`
- in `urls.py` add url to all urls in new app folder using `include()` function
## 4. Template
- Add templates in `APPNAME\templates\APPNAME`
- Use `render()` in views to point to template