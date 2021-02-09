# Project Description :
  As part of a small organization i want to give my users the ability to organize and exchange notes!

# Project dependencies : 
- Python version : 3.8.6
- Django : 3.1.4
- DRF : 3.12.2

# Virtual environment : 
- $ python3.8 -m venv venv (Note: 'python3.8-dev' and 'python3.8-venv' must be install)
- $ source venv/bin/activate 
- $ pip install -r requirements.txt

# Run project Locally :
- $ cd notes_sharing
- $ ./manage.py migrate
- $ ./manage.py createsuperuser
- $ ./manage.py runserver
- Running on http://localhost:8000 

# Note: 
  To access any api end point user must be logged-in with admin site.

# Database : 
  Sqlite DB 

# Base url :
  http://localhost:8000

# API ENDPOINTS: 
  There are three apps in the project. 
  1. users
  2. notes
  3. groups 

# API Documentation : 
  http://localhost:8000/api_doc/

# To Run TestCases use below command : 
  $ ./manage.py test

##Authentication: 
Token
