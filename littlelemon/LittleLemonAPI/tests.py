from django.test import TestCase
from .models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        value = "Pie : 80"
        item = MenuItem.objects.create(title="Pie", price=80, inventory=100)
        self.assertEqual(item, value)