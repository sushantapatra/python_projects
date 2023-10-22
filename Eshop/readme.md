# Django Eshop Application

## Getting Started

=> django-admin startproject Eshop
=> cd Eshop
=> django-admin startapp store
=> django-admin startapp orders
=> django-admin startapp profile

=> python manage.py runserver

## Generate Requirement.txt
=> pip freeze>requirements.txt
=> pip install requirements.txt

## create a migration file

=> python manage.py makemigrations
=> python manage.py migrate
"Default Databe Names [auth_groupm,auth_group_permissions,auth_permission,auth_user,auth_user_groups,auth_user_user_permissions,django_admin_log,django_content_type,django_migrations,django_session]"
=> python manage.py createsuperuser

### Prerequisites

python
django
mysqli

### Installation

pip install virtualenv
virtualenv venv
venv\Scripts\activate

pip install django
pip install mysqlclient

# Database Connection

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

""" DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
} """

# mysqli database connection

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'django_eshp',
'USER': 'root',
'PASSWORD': '',
'HOST': 'localhost',
'PORT': '3306',
'OPTIONS': {
'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
'charset': 'utf8mb4',
},
}
}

# PostgreSQL Database connection

""" DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'test',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': 'localhost',
'PORT': '5432'
}
} """

# MsSql Server Database connection

""" DATABASES = {
"default": {
"ENGINE": "mssql",
"NAME": "test",
"USER": "sa",
"PASSWORD": "sa@123",
"HOST": "localhost", # "PORT": "1433",
"OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", },
},
} """

# Showing Static Images

## project setting.py

STATIC_URL = 'static/'
MEDIA_URL = '/images/products/'
MEDIA_ROOT = BASE_DIR
STATIC_ROOT = 'static/'

## project urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
