import pytest
from rest_framework.test import APIClient
from logistic.models import Product
from django.contrib.auth.models import User


def test_simple():
    assert 2 == 2

def test_simple2():
    assert 2 == 2

# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('user', 'user@mail.com', 'password')
#     assert User.objects.count() == 1
#
# @pytest.fixture
# def client():
#     return APIClient()
#
#
# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('user', 'user@mail.com', 'password')
#     assert User.objects.count() == 1
#
#
# @pytest.mark.django_db
# def test_get_one_product():
#     client = APIClient()
#     Product.objects.create(title="огурец", description="божественный огурец")
#     responce = client.get('/api/v1/products/')
#     assert responce.status_code == 200

