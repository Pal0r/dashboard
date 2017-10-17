## Dashboard Development

1. Create a virtualenv:  
`mkvirtualenv dashboard_scraper`  

2. Install requirements:  
`pip install -r requirements.txt`  

3. Run migrations:  
`python manage.py migrate`  

4. Create a super user:  
`python manage.py createsuperuser`  

### Start the admin:  
`python manage.py runserver`  
Visit: 127.0.0.1:8000/admin/