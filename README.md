# PatientClerk
Patient Clerk is a django web application that helps doctors take and manage clinical patients' history and examination in a clean, intuitive and easy to follow interface.

## Project Decription
This is a web application built using the Django web framework version 4.2.2. The whole application has been built in a django environment including the frontend which is mainly comprised of Django's template system.

## Installation
- Make sure you have the latest version of Python and pip installed
- Make sure you have a DBMS like MySQL with root user access
- run the setup for the mysql database for this project - `./setup_mysql`
- Create a container directory on your machine eg `mkdir portfolio`
- Clone this repository unto your machine in the created repository
- `cd` into that directory
- Then run:
```
pip install requirements.txt
python manage.py migrate # Exports python classes as models to a database
python manage.py createsuperuser # You will be prompted for username, password etc, enter what you like
python manage.py runserver
```
This should start the web app on the local host

## Progress
This is still an ongoing project. Currently it runs on the local host but will soon be updated to run on a dedicated server for public access
There are still some unit tests to be pushed

## Credit
Some themes on the frontend were used from [Github](https://github.com/divanov11/StudyBud). These gave a base upon which customization was then done

## AUTHORS
Brilliant Chatuwa [Github](https://github.com/brilliantchats)

## LICENCE
Public Domain. No copy write protection.
