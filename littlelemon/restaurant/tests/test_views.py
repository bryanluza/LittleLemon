from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu
from ..serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuItemsViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create test menu items
        Menu.objects.create(title="Burger", price=8.99, inventory=30)
        Menu.objects.create(title="Pizza", price=12.99, inventory=20)

        # Initialize the APIClient
        self.client = APIClient()

        # Authenticate the test user
        self.client.force_authenticate(user=self.user)

        # Get the URL for the MenuItemsView
        self.url = reverse('menu-items')

    def test_getall(self):
        # Send GET request to retrieve all menu items
        response = self.client.get(self.url)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve all menu items from the database
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Check if the serialized data matches the response data
        self.assertEqual(response.data, serializer.data)

        # Check if the correct number of items is returned
        self.assertEqual(len(response.data), 2)

    def test_create_menu_item(self):
        # Data for a new menu item
        new_item_data = {
            "title": "Baklava",
            "price": "10.99",
            "inventory": 69
        }

        # Send POST request to create a new menu item
        response = self.client.post(self.url, new_item_data)

        # Check if the creation was successful (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the new item exists in the database
        self.assertTrue(Menu.objects.filter(title="Baklava").exists())

    # def test_authentication_required(self):
        # Log out the user
        self.client.force_authenticate(user=None)

        # Try to access the view without authentication
        response = self.client.get(self.url)

        # Check if the request was unauthorized (status code 401)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
