from django.test import TestCase
from ..models import Menu
from django.db import models

class MenuTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="IceCream",
            price=80,
            inventory=50
        )

    def test_get_item(self):
        self.assertTrue(isinstance(self.menu_item, Menu))
        self.assertEqual(self.menu_item.__str__(), "IceCream : 80")

    def test_title_max_length(self):
        max_length = self.menu_item._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_price_decimal_places(self):
        decimal_places = self.menu_item._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_inventory_is_smallinteger(self):
        self.assertIsInstance(self.menu_item._meta.get_field('inventory'), models.SmallIntegerField)

    def test_menu_fields(self):
        self.assertEqual(self.menu_item.title, "IceCream")
        self.assertEqual(self.menu_item.price, 80)
        self.assertEqual(self.menu_item.inventory, 50)
