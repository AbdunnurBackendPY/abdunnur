from unittest import TestCase

from django.test import SimpleTestCase

from .models import Cats


# class SimpleTests(SimpleTestCase):
#     def test_main_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)


class CatsTestCase(TestCase):
    def setUp(self):
        self.cats = Cats.objects.create(
            name='test',
            color='red',
            old=15)


    def test_name(self):
        self.assertEqual(str(self.cats.name),"test")



    def test_color(self):
        self.assertEqual(str(self.cats.color),"red")



    def test_old(self):
        self.assertEqual(str(self.cats.old),"15")