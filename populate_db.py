import django
import json

django.setup()

from django.utils.crypto import get_random_string

from supply.tests.factories import get_random_geo_polygon, get_random_service_price, get_random_phone_number



def get_suppliers_json_list():
    suppliers_json_list = []
    for idx in range(100):
        supplier_json = {
            "model": "supply.Supplier",
            "pk": idx + 1,
            "fields": {
                "title": get_random_string(),
                "email": "{}@example.com".format(get_random_string().lower()),
                "phone_number": get_random_phone_number(),
                "address": get_random_string()
            }
        }
        suppliers_json_list.append(supplier_json)
    return suppliers_json_list


def get_service_area_json_list():
    service_areas_json_list = []
    for idx in range(100):
        service_area_json = {
            "model": "supply.ServiceArea",
            "pk": idx + 1,
            "fields": {
                "title": get_random_string(),
                "poly": "{}".format(get_random_geo_polygon().json),
                "supplier": idx + 1
            }
        }
        service_areas_json_list.append(service_area_json)
    for idx in range(101, 1000):
        service_area_json_for_one_supplier = {
            "model": "supply.ServiceArea",
            "pk": idx,
            "fields": {
                "title": get_random_string(),
                "poly": "{}".format(get_random_geo_polygon().json),
                "supplier": 2
            }
        }
        service_areas_json_list.append(service_area_json_for_one_supplier)
    return service_areas_json_list


def create_fixture_json():
    new_fixture = []
    new_fixture += get_suppliers_json_list()

    new_fixture += get_service_area_json_list()
    # new_fixture += get_services_json()
    return new_fixture


if __name__ == '__main__':
    fixture = create_fixture_json()
    file = open('f.json', 'w')
    file.write(str(fixture))
