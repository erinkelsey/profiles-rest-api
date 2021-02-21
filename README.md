# Profiles REST API

REST API implemented with Django, Django REST Framework, Vagrant and SQLite that supports the following:

1. Creating new profiles
   - Handle registration of new users
   - Validate profile data
2. Listing existing profiles
   - Search for profiles by email and name
3. View specific profiles
   - Find by profile ID
4. Update profile of logged in user
   - Change name, email and password
   - Only the logged in user can change their profile info
5. Creating new feed items
   - Only when user is logged in
6. Updating feed items
   - Only when user is logged in
   - Only the user's feed items
7. Deleting feed items
   - Only when user is logged in
   - Only the user's feed items
8. Viewing other profile status updates
   - All user

### API Endpoints

<table>
    <thead>
        <tr>
            <th>Method</th>
            <th>Route</th>
            <th>Description</th>
            <th>Request Body</th>
        </tr>
    </thead>
    <tr>
        <td>GET</td>
        <td>/api/profile/</td>
        <td>List all profiles.</td>
        <td>None</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/api/profile/</td>
        <td>Create a new profile.</td>
        <td>Should be application/json. Fields: email, name, password</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/api/profile/:profileId/</td>
        <td>Get details for a specific profile.</td>
        <td>None</td>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/api/profile/:profileId/</td>
        <td>Replace a specific profile.</td>
        <td>Should be application/json. Fields: email, name, password</td>
    </tr>
    <tr>
        <td>PATCH</td>
        <td>/api/profile/:profileId/</td>
        <td>Partial update for specific profile.</td>
        <td>Should be application/json. Fields: email, name -> all optional</td>
    </tr>
    <tr>
        <td>DELETE</td>
        <td>/api/profile/:profileId/</td>
        <td>Deletes a specific profile.</td>
        <td>None</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/api/login/</td>
        <td>Login to with email and password to get authentication token.</td>
        <td>Should be application/json. Fields: email, password</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/api/feed/</td>
        <td>List all feed items.</td>
        <td>None</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/api/feed/</td>
        <td>Create a new feed item for logged in user.</td>
        <td>Should be application/json. Fields: </td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/api/feed/:feedItemId/</td>
        <td>Get a specific feed item's details.</td>
        <td>None</td>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/api/feed/:feedItemId/</td>
        <td>Replace a specific feed item. Only allowed for user that created the item.</td>
        <td>Should be application/json. Fields: </td>
    </tr>
    <tr>
        <td>PATCH</td>
        <td>/api/feed/:feedItemId/</td>
        <td>Partial update for specific feed item. Only allowed for user that created the item.</td>
        <td>Should be application/json. Fields:  -> all optional</td>
    </tr>
    <tr>
        <td>DELETE</td>
        <td>/api/feed/:feedItemId/</td>
        <td>Deletes a specific feed item. Only allowed for user that created the item.</td>
        <td>None</td>
    </tr>
</table>

##### Test With Django REST Framework browser app

You can test with the built-in Django REST Framework browser app, just go to:

    http://127.0.0.1:8088/api/profile/

##### Use with authentication token

- Login and receive an authentication token: http://127.0.0.1:8088/api/login/
- Use ModHeaders Chrome extension to add authentication header to all requests
- Make sure request headers is checked
- Set the 'Authorization' header to be 'Token [your_token]'

## Setup

### Vagrant

Start the Vagrant server:

    $ vagrant up

Connect to Vagrant:

    $ vagrant ssh

Go to project folder on Vagrant:

    $ cd /vagrant

### Virtual Environment

_NOTE: You will need the Vagrant server running_

Create virtual environment:

    $ python -m venv ~/env

Activate virtual environment:

    $ source ~/env/bin/activate

### Django

_NOTE: You will need the Vagrant server running and virtual environment activated_

Install requirements from requirements.txt:

    $ pip install -r requirements.txt

Run Django DB migrations:

    $ python manage.py migrate

Create Django superuser:

    $ python manage.py createsuperuser

_NOTE: you will need to add an email, name and password_

## Run

_NOTE: You will need the Vagrant server running and virtual environment activated_

Run Django server:

    $ python manage.py runserver 0.0.0.0:8088

Navigate to in web browser:

    http://127.0.0.1:8088

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

_NOTE: automatically synced with local project folder_

Stop Vagrant box:

    $ vagrant halt

Remove Vagrant box:

    $ vagrant destroy

Update Vagrant box image:

    $ vagrant box update

_NOTE: you must rebuild the image after updating_

### Virtual Environments

Create virtual environment:

    $ python -m venv ~/env

Activate virtual environment:

    $ source ~/env/bin/activate

Deactivate virtual environment:

    $ deactivate

### Django

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

_NOTE: you will need to add an email, name and password_

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

_NOTE: there is a test implementation on apiview-test branch_

#### ViewSets

What: Uses model operations for functions

How:

- List - Getting a list of objects (HTTP GET Method)
- Create - Creating new objects (HTTP POST Method)
- Retrieve - Getting a specific object (HTTP GET Method)
- Update - Updating an object (HTTP PUT Method)
- Partial Update - Updating part of an object (HTTP PATCH Method)
- Destroy - Deleting an object (HTTP DELETE Method)

Why:

- Takes care of a lot of the typical logic for you
- Perfect for standard database operations
- Fastest way to make a database interface

When:

- A simple CRUD interface to your database
- A quick and simple API to manage predefined objects
- Little to no customization on the logic
- Working with standard data structures
