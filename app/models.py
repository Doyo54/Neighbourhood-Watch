from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/',default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=60, blank=True)
    neighbourhood = models.ForeignKey("Neighbourhood", on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile_picture=value)

    def save_profile(self):
        self.name

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood', default='1')
    logo = models.ImageField(upload_to='images/',default='default.png')
    description = models.TextField()
    health_tell = models.IntegerField(null=True, blank=True)
    occupants = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.name

    def delete_neighborhood(self):
        self.delete()
    
    def get_hood(self):
        hood = Neighbourhood.objects.all()
        return hood

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    @classmethod
    def update_occupants(cls, occupants, value):
        cls.objects.filter(occupants=occupants).update(occupants=value)
    
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')


class Business(models.Model):
    name = models.CharField(max_length=150, verbose_name='Business Name', null=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    email = models.CharField(max_length=150, verbose_name='Business Email Address', null=True, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, verbose_name='NeighbourHood', null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Business Owner')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.name)

    def get_businesses(self):
        businesses = Business.objects.all()
        return businesses

    def create_business(self):
        self.name

    def delete_business(self):
        self.delete()

    def find_business(self,business_id):
        business = Business.objects.filter(self = business_id)
        return business

    def update_business(self):
        
        self.update()
    
    class Meta:
        verbose_name_plural = 'Businesses'


