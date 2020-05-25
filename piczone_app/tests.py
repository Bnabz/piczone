from django.test import TestCase
from .models import Image, Category, Location
import datetime as dt

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Kenya')
        self.location.save_location()

        self.category = Category(name='nature')
        self.category.save_category()

        self.image_test = Image( image = image='test.jpg'name='test_name', description='test_description', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_method(self):
        self.photo.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)


