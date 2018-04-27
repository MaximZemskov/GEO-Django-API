# JSON REST API

API allows you to mark **service areas** on a map and filter them by point intersection and title of service.


## Installation

```sh
$ git clone https://github.com/MaximZemskov/JSON-REST-API.git
$ cd JSON-REST-API
$ pip install requirements.txt
$ python manage.py runserver
```

## API
 + List of suppliers(GET). Create supplier(POST)
    + [['GET', 'POST'] http://localhost:8000/api/suppliers/](http://localhost:8000/api/suppliers/)
 + Detail supplier(GET). Update supplier(PUT, PATCH) 
    + [['GET', 'PUT', 'PATCH'] http://localhost:8000/api/suppliers/<int:id>/](http://localhost:8000/api/suppliers/1/)
 + List of service areas(GET). Create service area(POST) 
    + [['GET', 'POST'] http://localhost:8000/api/service_areas/](http://localhost:8000/api/service_areas/)
 + Detail service area(GET). Update service area(PUT, PATCH)  
    + [['GET', 'PUT', 'PATCH'] http://localhost:8000/api/service_areas/<int:id>](http://localhost:8000/api/suppliers/1/)
 + List of services(GET). Create service(POST)
    + [['GET', 'POST'] http://localhost:8000/api/services/](http://localhost:8000/api/services/)
 + Detail service(GET). Update service(PUT, PATCH)  
   + [['GET', 'PUT', 'PATCH'] http://localhost:8000/api/services/<int:id>](http://localhost:8000/api/services/1/)
   
## Example
[GET: http://localhost:8000/api/suppliers/](http://localhost:8000/api/suppliers/)

```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "url": "http://127.0.0.1:8000/api/suppliers/2/",
            "title": "qwe",
            "email": "qwe@asd.com",
            "phone_number": "wqe",
            "address": "asd 12"
        },
        {
            "id": 3,
            "url": "http://127.0.0.1:8000/api/suppliers/3/",
            "title": "1aw",
            "email": "asd@asd.com",
            "phone_number": "12312123",
            "address": "12312 asd 1212"
        },
        {
            "id": 4,
            "url": "http://127.0.0.1:8000/api/suppliers/4/",
            "title": "Pool",
            "email": "ads@pool.com",
            "phone_number": "123321",
            "address": "1123 qww"
        },
        {
            "id": 5,
            "url": "http://127.0.0.1:8000/api/suppliers/5/",
            "title": "123",
            "email": "qwe@qadw.com",
            "phone_number": "123123",
            "address": "sdasad"
        },
        {
            "id": 6,
            "url": "http://127.0.0.1:8000/api/suppliers/6/",
            "title": "adsad",
            "email": "1eqasd@asd.com",
            "phone_number": "ad1212312",
            "address": "123123123"
        }
    ]
}
```
[POST: http://localhost:8000/api/suppliers/](http://localhost:8000/api/suppliers/)
data:
```json
{
    "title": "new title",
    "email": "newemail@m.com",
    "phone_number": "9999999999",
    "address": "pik street 8"
}
```

