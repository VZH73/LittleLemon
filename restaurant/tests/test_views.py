from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=50, inventory=20)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        response = self.client.get(reverse('menu_items'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_items.data)