# Project Little Lemon

## Static Content
- **Homepage:** [http://localhost:8000/restaurant/](http://localhost:8000/restaurant/)

## API Endpoints
- **Menu**: `[GET, POST]` [http://localhost:8000/restaurant/menu/](http://localhost:8000/restaurant/menu/)
- **Menu items**: `[GET, PUT, PATCH, DELETE]` [http://localhost:8000/restaurant/menu/{menuId}](http://localhost:8000/restaurant/menu/{menuId})
- **Booking**: `[GET, POST]` [http://localhost:8000/restaurant/booking/table](http://localhost:8000/restaurant/booking/table)
- **Create Tokens**: `[POST]` [http://127.0.0.1:8000/restaurant/api-token-auth/](http://127.0.0.1:8000/restaurant/api-token-auth/)

## Project Setup

### Pipenv
- **Install pipenv:** `pip install pipenv`
- **Create & activate virtual environment:** `pipenv shell`
- **Install requirements:** `pipenv install`
- **Exit virtual environment:** `exit`

### Django Commands
- **Create a project:** `django-admin startproject projectname`
- **Create an app:** `python manage.py startapp appname`
- **Create migrations:** `python manage.py makemigrations`
- **Apply migrations:** `python manage.py migrate`
- **Create superuser:** `python manage.py createsuperuser`
- **Start development server:** `python manage.py runserver`
