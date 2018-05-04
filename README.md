# JSON REST API

API allows you to mark **service areas** on a map and filter them by point intersection and title of service.

Example:
+ [http://mzemskov.com/selection/?x=0&y=0](http://mzemskov.com/selection/?x=0&y=0) - Selection suppliers by latitude, longtitude and 
service title
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
$ export DJANGO_SETTINGS_MODULE=JsonRestApi.settings
$ pytest
```

## Populate database
```bash
$ export DJANGO_SETTINGS_MODULE=JsonRestApi.settings
$ python manage.py populate_db.py
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
   
## Example

[GET: http://127.0.0.1:8000/api/selection/?x=0&y=0&title=new service 1](http://127.0.0.1:8000/api/selection/?x=value&y=value&title=value)
response:
```json
[
    {
        "title": "1aw",
        "areas": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    -24.535633027553555,
                                    16.073793204512057
                                ],
                                [
                                    33.68628412485123,
                                    6.084909356168231
                                ],
                                [
                                    23.990892469882954,
                                    -34.98455647902815
                                ],
                                [
                                    -21.31110280752182,
                                    -37.22338469506037
                                ],
                                [
                                    -24.535633027553555,
                                    16.073793204512057
                                ]
                            ]
                        ]
                    },
                    "properties": {
                        "title": "new area",
                        "services": [
                            {
                                "title": "new service 1",
                                "price": "1005001050"
                            },
                            {
                                "title": "йцуas",
                                "price": "1200"
                            },
                            {
                                "title": "new service2",
                                "price": "100500"
                            }
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "geometry": null,
                    "properties": {
                        "title": "фывфывф",
                        "services": [
                            {
                                "title": "asdasd",
                                "price": "1231"
                            }
                        ]
                    }
                }
            ]
        }
    }
]
```

[POST: http://localhost:8000/api/suppliers/](http://localhost:8000/api/suppliers/)
data:
```json
{
    "title": "new title",
    "email": "newemail@m.com",
    "phone_number": "+79999999999",
    "address": "pik street 8"
}
```

[PUT: http://localhost:8000/api/suppliers/<int:id>](http://localhost:8000/api/suppliers/<int:id>)
data:
```json
{
    "id": 22,
    "title": "John",
    "email": "john@example.com",
    "phone_number": "+94457345439",
    "address": "9477 Cooke Roads\nNew Morganside, TX 30949-4854"
}
```

[POST: http://localhost:8000/api/service_areas/](http://localhost:8000/api/service_areas/)
```json
{
    "services": [],
    "title": "Some title",
    "poly": poly in geojson,
    "supplier": supplier_id
}
```

[PUT: http://localhost:8000/api/service_areas/<int:id>](http://localhost:8000/api/service_areas/<int:id>)
```json
{
    "id": 23,
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    -90.0,
                    87.0
                ],
                [
                    -85.0,
                    92.0
                ],
                [
                    -89.0,
                    83.0
                ],
                [
                    -87.0,
                    84.0
                ],
                [
                    -87.0,
                    82.0
                ],
                [
                    -90.0,
                    87.0
                ]
            ]
        ]
    },
    "properties": {
        "url": "http://127.0.0.1:8000/api/service_areas/23/",
        "services": [
            {
                "id": 17,
                "url": "http://127.0.0.1:8000/api/services/17/",
                "title": "Brian",
                "price": "538438",
                "service_area": 23
            }
        ],
        "title": "Mcmillan",
        "supplier": 31
    }
}
```

[POST: http://localhost:8000/api/services/](http://localhost:8000/api/services/)
data:
```json
{
    "title": "Title",
    "price": "1230",
    "service_area": service_area_id
}
```

[PUT: http://localhost:8000/api/services/<int:id>](http://localhost:8000/api/services/<int:id>)
data:
```json
{
    "id": 21,
    "url": "http://127.0.0.1:8000/api/services/21/",
    "title": "asdasd",
    "price": "1231",
    "service_area": 26
}
```



