## ================= Online Couse Selling =======================

## =>Users
first_name
last_name
email
password


## =>Courses
name
description
price
discount
active
thumbnail
resource
course_length


## =>Tags
tag
Course(Fk)

## =>Prerequisites
prerequisites
Course(Fk)


## =>Learnings
learning
Course(Fk)

## =>Vedeos
title
Course(Fk)
serial_number
url
is_preview



## =>UserCourse
UserCourse(Fk)
Course(Fk)
date


## =>Payments
payment_id
request_id
status
UserCourse(Fk)
date


## ============= Start Project ==============
django-admin startproject onlinecourse
django-admin startapp courses
=> register your app
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser



pip install django-bootstrap-v5
register in app

Use in html file
{% load bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}

## Get all videos in course 
course = Course.objects.filter(slug=slug) # get multiple record
course = Course.objects.get(slug=slug) # get single record
<p>{{ course.video_set.all}}</p>
<p>{{ course.tag_set.all}}</p>
<p>{{ course.prerequisite_set.all}}</p>
<p>{{ course.learning_set.all}}</p>


