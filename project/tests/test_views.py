from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from project.views import product_detail
from django.contrib.auth.models import User, AnonymousUser
import pytest
from django.test import TestCase


# @pytest.mark.django_db
# class TestViews(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super(TestViews, cls).setUpClass()
#         mixer.blend('project.Product')
#         cls.factory = RequestFactory()
#
#     def test_product_detail_authenticated(self):
#         path = reverse('detail', kwargs={'pk': 1})
#         request = self.factory.get(path)
#         request.user = mixer.blend(User)
#
#         response = product_detail(request, pk=1)
#         assert response.status_code == 200
#
#     def test_product_detail_unauthenticated(self):
#         path = reverse('detail', kwargs={'pk': 1})
#         request = self.factory.get(path)
#         request.user = AnonymousUser()
#
#         response = product_detail(request, pk=1)
#         assert response.status_code == 302

@pytest.fixture
def factory():
    return RequestFactory()

@pytest.fixture
def product(db):
    return mixer.blend('project.Product')


def test_product_detail_authenticated(factory, product):
    mixer.blend('project.Product')
    path = reverse('detail', kwargs={'pk': 1})
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = product_detail(request, pk=1)
    assert response.status_code == 200

def test_product_detail_unauthenticated(factory, product):
    mixer.blend('project.Product')
    path = reverse('detail', kwargs={'pk': 1})
    request = factory.get(path)
    request.user = AnonymousUser()

    response = product_detail(request, pk=1)
    assert response.status_code == 302