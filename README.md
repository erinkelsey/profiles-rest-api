# Profiles REST API

REST API implemented with Django, Django REST Framework, Vagrant and SQLite.

## Setup

### Vagrant

Start the Vagrant server:

    $ vagrant up

Connect to Vagrant:

    $ vagrant ssh

### Django

NOTE: You will need the Vagrant server running

Run Django DB migrations:

    $ python manage.py migrate

Create Django superuser:

    $ python manage.py createsuperuser

NOTE: you will need to add an email, name and password

## Run

NOTE: You will need the Vagrant server running

Run Django server:

    $ python manage.py runserver 0.0.0.0:8088

Navigate to in web browser:

    http://127.0.0.1:8088

## Test

## Build

## Deploy

## Notes

### Vagrant

Initialize project with a Vagrantfile based on Ubuntu Bionic64 OS:

    $ vagrant init ubuntu/bionic64

Start the Vagrant server:

    $ vagrant up

Connect to Vagrant:

    $ vagrant ssh

Disconnect from Vagrant:

    > exit

Project folder on Vagrant:

    $ cd /vagrant

NOTE: automatically synced with local project folder.

### Setup Django Project

Create virtual environment:

    $ python -m venv ~/env

Activate virtual environment:

    $ source ~/env/bin/activate

Deactivate virtual environment:

    $ deactivate

Install requirements from requirements.txt:

    $ pip install -r requirements.txt

Create Django project:

    $ django-admin.py startproject [project-name] .

Create a Django app within the Django project:

    $ python manage.py startapp [app-name]

Install the Django app and the apps from requirements.txt in the project settings.py file

Run Django server:

    $ python manage.py runserver 0.0.0.0:8088

Navigate to in web browser:

    http://127.0.0.1:8088

Create DB migrations:

    $ python manage.py makemigrations

Migrate migrations:

    $ python manage.py migrate

Create Django superuser:

    $ python manage.py createsuperuser

NOTE: you will need to add an email, name and password

Login to Django admin portal using superuser credentials:

    http://127.0.0.1:8088/admin/
