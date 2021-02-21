# Profiles REST API

REST API implemented with Django, Django REST Framework, Vagrant and SQLite.

## Setup

### Vagrant

Start the Vagrant server:

    $ vagrant up

Connect to Vagrant:

    $ vagrant ssh

Go to project folder on Vagrant:

    $ cd /vagrant

### Django

NOTE: You will need the Vagrant server running

Create virtual environment:

    $ python -m venv ~/env

Activate virtual environment:

    $ source ~/env/bin/activate

Install requirements from requirements.txt:

    $ pip install -r requirements.txt

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

Shutdown Vagrant server:

    $ vagrant halt

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

If it keeps automatically reloading:

    $ python manage.py runserver 0.0.0.0:8088 --noreload

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

### Django REST Framework Views

#### APIView

What: Describes logic to make an API endpoint.

How:

- Get - Return one or more items
- Post - Create an item
- Put - Update an item
- Patch - Partially update an item
- Delete - Delete an item

Why: Gives the most control over logic:

- Perfect for implementing complex logic
- Calling other APIs
- Working with local files

When: To use APIViews

- Need full control over the logic
- Processing files and rendering a synchronous response
- You are calling other (external) APIs/service
- Accessing local files or data

NOTE: there is a test implementation on ... branch
