import pytest
from django.utils.crypto import get_random_string
from django.contrib.gis.geos import Polygon, Point

from rest_framework.test import APIClient
from rest_framework import status

from .fixtures import create_user
from .factories import (
    get_random_geo_polygon,
    get_random_service_price,
    SupplierFactory,
    ServiceAreaFactory,
    ServiceFactory
)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def api_client():
    user = create_user()
    client = APIClient()
    client.force_login(user)
    client.user = user
    return client


@pytest.mark.django_db
def test_api_selection_unauthorized(client):
    supplier = SupplierFactory.create()

    x = 0
    y = 0

    test_poly = Polygon(((-8, 7), (17, 7), (16, -18), (-15, -18), (-8, 7)))

    service_area = ServiceAreaFactory.create(supplier=supplier, poly=test_poly)
    service = ServiceFactory.create(service_area=service_area)

    res = client.get('/api/selection/?x={}&y={}'.format(x, y))
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_selection_with_one_poly(api_client):
    supplier = SupplierFactory.create()

    x = 0
    y = 0

    test_poly = Polygon(((-8, 7), (17, 7), (16, -18), (-15, -18), (-8, 7)))

    service_area = ServiceAreaFactory.create(supplier=supplier, poly=test_poly)

    res = api_client.get('/api/selection/?x={}&y={}'.format(x, y))
    assert res.status_code == status.HTTP_200_OK
    assert res.data['count'] == 1


@pytest.mark.django_db
def test_api_selection_with_few_poly(api_client):
    supplier_1 = SupplierFactory.create()
    supplier_2 = SupplierFactory.create()

    x = 0
    y = 0

    test_poly_1 = Polygon(((-8, 7), (17, 7), (16, -18), (-15, -18), (-8, 7)))
    test_poly_2 = Polygon(((-6., 8), (17, 7), (15, -11), (-12, -10), (-6, 8)))

    service_area_1 = ServiceAreaFactory.create(supplier=supplier_1,
                                               poly=test_poly_1)
    service_area_2 = ServiceAreaFactory.create(supplier=supplier_2,
                                               poly=test_poly_2)

    res = api_client.get('/api/selection/?x={}&y={}'.format(x, y))
    assert res.status_code == status.HTTP_200_OK
    assert res.data['count'] == 2


@pytest.mark.django_db
def test_api_selection_with_few_poly_and_titles(api_client):
    supplier_1 = SupplierFactory.create()
    supplier_2 = SupplierFactory.create()

    x = 0
    y = 0

    test_poly_1 = Polygon(((-8, 7), (17, 7), (16, -18), (-15, -18), (-8, 7)))
    test_poly_2 = Polygon(((-6., 8), (17, 7), (15, -11), (-12, -10), (-6, 8)))

    service_area_1 = ServiceAreaFactory.create(supplier=supplier_1,
                                               poly=test_poly_1)
    service_area_2 = ServiceAreaFactory.create(supplier=supplier_2,
                                               poly=test_poly_2)

    service_1 = ServiceFactory.create(service_area=service_area_1)
    service_2 = ServiceFactory.create(service_area=service_area_2)

    test_title = service_1.title

    res = api_client.get('/api/selection/?x={}&y={}&title={}'.format(
        x, y, test_title))
    assert res.status_code == status.HTTP_200_OK
    assert res.data['count'] == 1
    assert res.data['results'][0]['areas']['features'][0]['properties'][
               'services'][0]['title'] == test_title


@pytest.mark.django_db
def test_api_selection_with_miss_poly(api_client):
    supplier = SupplierFactory.create()

    x = 0
    y = 0

    test_poly = Polygon(((11, 20), (20, 40), (21, 30), (30, 10), (11, 20)))

    service_area = ServiceAreaFactory.create(supplier=supplier,
                                             poly=test_poly)

    res = api_client.get('/api/selection/?x={}&y={}'.format(x, y))
    assert res.status_code == status.HTTP_200_OK
    assert res.data['count'] == 0
