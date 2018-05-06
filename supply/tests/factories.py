import random

import factory
from django.contrib.gis.geos import Polygon, Point

from supply.models import Supplier, ServiceArea, Service


def get_random_phone_number():
    return '+{}'.format(random.randint(79068077767, 99968077767))


def get_random_geo_polygon():
    count = random.randint(2, 5)
    first_point = Point(
        random.randint(-90, 90),
        random.randint(-90, 90), srid=4326
    )
    last_point = first_point

    polys_points = ()
    for _ in range(count):
        while True:
            point = Point(
                first_point.x + random.randint(-5, 5),
                first_point.y + random.randint(-5, 5),
                srid=4326
            )
            if not first_point.equals(point):
                polys_points += (point,)
                break
    poly = (first_point,) + polys_points + (last_point,)
    return Polygon(poly, srid=4326)


def get_random_service_price():
    return '{}'.format((random.randint(1, 1200000)))


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    title = factory.Faker('first_name')
    phone_number = factory.LazyAttribute(lambda x: get_random_phone_number())
    email = factory.LazyAttribute(
        lambda x: '{}@example.com'.format(x.title).lower()
    )
    address = factory.Faker('address')


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceArea

    title = factory.Faker('last_name')
    poly = factory.LazyAttribute(lambda x: get_random_geo_polygon())
    supplier = factory.SubFactory(SupplierFactory)


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    title = factory.Faker('first_name')
    price = factory.LazyAttribute(lambda x: get_random_service_price())
    service_area = factory.SubFactory(ServiceAreaFactory)
