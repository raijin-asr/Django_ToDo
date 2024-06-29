# Django_ToDo

# Cretaing virtual env and installing packages
    -This is one time steup
    1. Python -m venv todoEnv
    2. Set-ExecutionPolicy Unrestricted Scope Process (if problem occurs and cant activate)
    3. todoEnv\Scripts\activate
    4. pip freeze
    5. pip install django
    6. pip freeze (to see if django installed)

# Creating Project and app, migrate db
    7. django-admin startproject djangoToDo
    8. django-admin startapp taskToDo 
    9. ls (see if there is manage.py in the list)
    10. python manage.py migrate(optional)

# Running Application
    12. python manage.py runserver

# Note:
    13. Add templates and static folder in taskToDo
