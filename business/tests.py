from django.test import TestCase
from .models import Business, Profile
from django.contrib.auth.models import User

user = User.objects.get(id=1)
profile = Profile.objects.get(id=1)

# Create your tests here.
class TestBusiness(TestCase):
    def setUp(self):
        self.new_business=Business(name = "", description="utawala", email='Nairobi', owner=profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_business(self):
        new_biz=self.new_business
        new_biz.create_business()
        posts=Business.get_businesses(self)
        self.assertTrue(len(posts)>0)

    def update_business(self):
        new_biz=self.new_business
        new_biz.update_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)

    def test_delete_business(self):
        new_biz=self.new_business
        new_biz.delete_business(self)
        new_biz.delete()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)
