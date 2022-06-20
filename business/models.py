from django.db import models
from django.contrib.auth.models import User

# Create your models here.
COUNTIES = [
    ('', ('Choose')), 
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CHOICES = [
    ('1', 'Crimes and Safety'),
    ('2', 'Health Emergency'),
    ('3', 'Recommendations'),
    ('4', 'Fire Breakouts'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
]
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=150, verbose_name='Business Name', null=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    email = models.CharField(max_length=150, verbose_name='Business Email Address', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Business Owner')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.name)

    def get_businesses(self):
        businesses = Business.objects.all()
        return businesses

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self,business_id):
        business = Business.objects.filter(self = business_id)
        return business

    def update_business(self):
        
        self.update()
    
    class Meta:
        verbose_name_plural = 'Businesses'


class Post(models.Model):
    title = models.CharField(max_length=120, null=True, verbose_name='Post Title')
    description = models.TextField(null=True, verbose_name='Post Description')
    category = models.CharField(max_length=120, choices=CHOICES, verbose_name='Post Category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Post Author')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'Posts'