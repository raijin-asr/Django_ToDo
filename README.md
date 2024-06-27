# Django_ToDo

# Cretaing virtual env and installing packages
    -This is one time steup
    1. Python -m venv todoEnv
    2. Set-ExecutionPolicy Unrestricted Scope Process (if problem occurs and cant activate)
    3. todoEnv\Scripts\activate
    4. pip freeze
    5. pip install django
    6. pip freeze (to see django installed)

# Creating Project and app, migrate db
    7. django-admin startproject djangoToDo
    8. cd djangoToDo
    9. django-admin startapp taskToDo 
    10. ls
    12. python manage.py migrate

# Running Application
    13. python manage.py runserver

# Note:
    14. Add templates and static folder in taskToDo
