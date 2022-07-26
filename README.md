# adevolutio_recruitiment_challenge
Developed an API using pyhton and Django with two GET endpoints. Each endpoint should query data from two JSONs (Orders and Deliveries). The API extracts the JSON content and query data from it.
--##----##----##----##----##----##----##--

Python version: 3.10.5
Django version: 4.0.6

--##----##----##----##----##----##----##--


The challenge required an API with two GET endpoits:

1- With order brand_id as a query parameter, return a list of orders and its deliveries; 
[SOLUTION] [.../order/?id=x] as request, it will extract the raw data and query with brand_id the required data.

2- With an id or reference of order as a query parameter, return the quantity of each product of that order that has already been shipped. 
[SOLUTION] [.../orders/products/?reference=x] or [.../orders/products/?id=x] as request, it will extract the raw data and query with order reference or order id the required data. 

!! ATTENTION !!
If you use PostMan, you won't have this problem.
If you are going to request data from this API using web browser, do not use # in reference, instead use %23, otherwise it wont work. 



--##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##--##----##--##----##--##----##--##----##--



If you have problems running the project try building a new project and copy the code in views.py and urls.py for the corresponding python file in the new project.

To build a new project using django and python:
1- Create a directory
2- go to cmd, open the created directory and execute py -m venv ./venv
3- cd .../venv/Scripts
4- ./activate
5- pip install django
6- pip install djangorestframework
7- pip install markdown       
8- pip install django-filter
9- django-admin startproject 'projectName'
10- cd .../'projectName'
11- python manage.py startapp 'appName'
12- in 'appName'.views.py, copy the code in the this project views.py
13- in 'projectName'.urls.py copy the code in the this project urls.py
14- python manage.py runserver


In the Django project, the whole code is in views.py and urls.py, there you will find the functions and classes used in the project.

--##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##----##--##----##--##----##--##----##--##----##--
