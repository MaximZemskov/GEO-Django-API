# GEO Django

API allows you to mark **service areas** on a map and filter them by point intersection and title of service.

Example:
+ [http://mzemskov.com/api/selection/?x=-26&y=73](http://mzemskov.com/api/selection/?x=-26&y=73) - Selection suppliers by latitude, longtitude and service title
+ [http://mzemskov.com/login/](http://mzemskov.com/login/) - login 
(credentioals: test/secret_test)
+ [http://mzemskov.com/api/suppliers/](http://mzemskov.com/api/suppliers/) -
 Suppliers list
+ [http://mzemskov.com/api/service_areas/](http://mzemskov.com/api/service_areas/) - Service areas list
+ [http://mzemskov.com/api/services/](http://mzemskov.com/api/services/) - Service list

![Need to fix problems](https://www.meme-arsenal.com/memes/42a6a91a55abd28ea9a2d1583e5fcacd.jpg)

## Installation

```sh
$ git clone https://github.com/MaximZemskov/JSON-REST-API.git
$ cd JSON-REST-API
$ pip install requirements.txt
$ python manage.py runserver
```

## Tests
```bash
$ pytest
```

## Populate database
```bash
$ python populate_db.py
$ tr \'\" \"\' < f.json > f1.json && rm f.json && mv f1.json fixture.json
$ python manage.py loaddata fixture.json 
```

## Authenticate
Create superuser
```bash
$ python manage.py createsuperuser
```
Open [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/) and 
provide login information

## API
 + Get selection of service areas by coordinates and service title
    + [GET: http://127.0.0.1:8000/api/selection/?x=value&y=value&title=value](http://127.0.0.1:8000/api/selection/?x=value&y=value&title=value)
 + List of suppliers(GET). Create supplier(POST)
    + [['GET', 'POST'] http://localhost:8000/api/suppliers/](http://localhost:8000/api/suppliers/)
 + Detail supplier(GET). Update supplier(PUT, PATCH) 
    + [['GET', 'PUT', 'PATCH'] http://localhost:8000/api/suppliers/<int:id>/](http://localhost:8000/api/suppliers/1/)
 + List of service areas(GET). Create service area(POST) 
    + [['GET', 'POST'] http://localhost:8000/api/service_areas/](http://localhost:8000/api/service_areas/)
 + Detail service area(GET). Update service area(PUT, PATCH)  
    + [['GET', 'PUT', 'PATCH'] http://localhost:8000/api/service_areas/<int:id>/](http://localhost:8000/api/suppliers/1/)
 + List of services(GET). Create service(POST)
    + [['GET', 'POST'] http://localhost:8000/api/services/](http://localhost:8000/api/services/)
 + Detail service(GET). Update service(PUT, PATCH)  
   + [['GET', 'PUT', 'PATCH'] http://localhost:8000/api/services/<int:id>/](http://localhost:8000/api/services/1/)
   




