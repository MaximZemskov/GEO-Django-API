import django
django.setup()

from supply.tests.factories import SupplierFactory, ServiceAreaFactory, Service


def get_random_supplier_json():
    supplier_json = {
        "title": "",
        "email": "",
        "phone_number": "",
        "address": ""
    }

def create_fixture_json():
    for idx in range(100):
        try:
            SupplierFactory()
            ServiceAreaFactory()
            Service()
        except:
            pass
    return True


if __name__ == '__main__':
    fixture = create_fixture_json()
    # file = open('fixture.json', 'w')
    # file.write(file)
