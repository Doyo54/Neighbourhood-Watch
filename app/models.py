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
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    @classmethod
    def update_occupants(cls, occupants, value):
        cls.objects.filter(occupants=occupants).update(occupants=value)