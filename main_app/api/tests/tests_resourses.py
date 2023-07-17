import json
from django.test import TestCase, Client

from main_app.api.resourses import ProductModelViewSet
from main_app.models import CustomUser, Product, Purchase, Returns
from rest_framework import status
from django.urls import reverse
from main_app.api.serializers import CustomUserSerializer, ProductSerializer, PurchaseSerializer, ReturnsSerializer

# initialize the APIClient app
client = Client()


class GetAllProductTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            name_of_product='Pasta', description='true product from Italy', price=165.0, quantity=38)
        Product.objects.create(
            name_of_product='Apperol', description='vol 40%, product from Italy', price=670.0, quantity=93)
        Product.objects.create(
            name_of_product='Shveps', description='water from coctaile', price=70.0, quantity=123)
        Product.objects.create(
            name_of_product='Potato', description='farmer product', price=50.0, quantity=223)
        Product.objects.create(
            name_of_product='Fish', description='fresh fish from Norway', price=740.0, quantity=53)

    #def test_get_all_products(self):
        # get API response
        #response = client.get('/product/')
        #response = ProductModelViewSet()(request)
        # get data from db
        ##products = Product.objects.all()
        #serializer = ProductSerializer(products, many=True)
        #response = self.client.get(url, data, format='json')
        #self.assertEqual(response.data, serializer.data)
        #self.assertEqual(response.status_code, status.HTTP_200_OK)

        #response = client.get(reverse('get_post_puppies'))

