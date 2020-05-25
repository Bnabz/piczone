from django.test import TestCase
from .models import Image, Category, Location
import datetime as dt

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='kenya')
        self.location.save_location()

        self.category = Category(name='nature')
        self.category.save_category()

        self.image_test = Image(id=1,image='test.jpg',name='test_name', description='test_description', location=self.location,
                                category=self.category)
        
        self.image_test.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_search_image_by_category(self):
        category = 'nature'
        image= self.image_test.search_image_by_category(category)
        self.assertTrue(len(image) > 0)

    
    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='kenya')
        self.assertTrue(len(found_images) > 0)

    def test_update_image(self):
        self.image_test.update_image(self.image_test.id, 'update_test.jpg')
        new_image = Image.objects.filter(image='update_test.jpg')
        self.assertTrue(len(new_image) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


class TestCategory(TestCase):
    def setUp(self):
        self.category = Category(name='cars')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    


