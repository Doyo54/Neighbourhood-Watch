from django.test import TestCase
from .models import Business, Profile,Neighbourhood
from django.contrib.auth.models import User

user = User.objects.get(id=1)
profile = Profile.objects.get(id=2)

# Create your tests here.
class TestBusiness(TestCase):
    def setUp(self):
        self.profile = Profile(name='doyo')
        self.new_business=Business(id=1,name = "", description="utawala", email='Nairobi', owner=self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_business(self):
        new_biz=self.new_business
        new_biz.create_business()
        posts=Business.get_businesses(self)
        self.assertTrue(len(posts)==0)

    def update_business(self):
        new_biz=self.new_business
        new_biz.update_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)

    def test_delete_business(self):
        new_biz=self.new_business
        new_biz.delete_business()
        posts=Business.get_businesses(self)
        self.assertTrue(len(posts)==0)
    
    def tearDown(self):
        Business.objects.all().delete()
        Profile.objects.all().delete()
    
class testNeighbourhood(TestCase):
    def setUp(self):
        self.profile = Profile(name='doyo')
        self.profile.save_profile()

        self.hood_test = Neighbourhood(id=1, name='food', location='Kilimani',user=self.profile,
                                logo= 'default.png',description='Nice Hood', health_tell=1110366,occupants=100,police_number=1234566)
        self.hood_test.create_neighborhood()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood_test, Neighbourhood))

    def test_delete_hood(self):
        new_hood=self.hood_test
        new_hood.delete_neighborhood()
        posts=Neighbourhood.get_hood(self)
        self.assertTrue(len(posts)==0)

    def update_occupants(self):
        new_hood=self.hood_test
        new_hood.update_occupants()
        posts=Neighbourhood.get_hood()
        self.assertTrue(len(posts)==0)

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='doyo')
        self.user.save()

        self.profile_test = Profile(id=10, name='image', profile_picture='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) == 0)
    
    def test_update_profile(self):
        self.profile_test.save_profile()
        self.profile_test.update_profile(self.profile_test.id, 'image/test.jpg')
        changed_img = Profile.objects.filter(profile_picture='image/test.jpg')
        self.assertTrue(len(changed_img) == 0)