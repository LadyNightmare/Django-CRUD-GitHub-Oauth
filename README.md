# Django-CRUD-GitHub-Oauth

![](./interviewproject/coverage.svg)

This application is a basic Django app in which an user can log in via GitHub. When the user firstly enters the app,
it asks to create a personal info profile with name, surname and some other personal data.

After the creation, the user can update the provided information. Whenever the user wants, data can be deleted and 
then created once again.

## HOW TO RUN IT

1. Clone the repository.
2. Create a virtual enviroment with Python 3.8.
3. Install the requirements from requirements.txt.
4. Create _interviewproject/interviewproject/secrets.py_ with the following content:
```
GITHUB_KEY = <your_app_key>
GITHUB_SECRET = <your_app_secret>
```
5. Create the application's migration files using the following command:
```
cd interviewproject
python manage.py makemigrations personalinfo
```
6. Apply the migrations with the following command:
```
python manage.py migrate
```
7. Run the server and enjoy the application ;)
```
python manage.py runserver 
```

## HOW TO RUN TESTS

```
python manage.py test 
```

To check the project tests coverage, run:
```
coverage run --source="." manage.py test personalinfo ; coverage report 
```

This is the current coverage report:
```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
personalinfo/admin.py        3      0   100%
personalinfo/apps.py         4      0   100%
personalinfo/forms.py       15      0   100%
personalinfo/models.py      25      0   100%
personalinfo/urls.py         4      0   100%
personalinfo/views.py       40      0   100%
------------------------------------------------------
TOTAL                       91      0   100%

```