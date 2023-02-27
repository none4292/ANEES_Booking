from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils import timezone
# Create your models here.
GENDER = (
    ('male','male'),
    ('female','female'),
)
TYPE = (
    ('seeker','seeker'),
    ('seracher','seracher')
)
class Roommset(models.Model):
    seeker = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=12000)
    price = models.IntegerField()
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propery/')
    created_at = models.DateTimeField(default=timezone.now)
    avablie_at = models.DateTimeField(blank=True, null=True)
    gender =  models.CharField(max_length = 50, choices = GENDER)
    lifestaly = models.TextField(max_length=750)
    type_seeker = models.CharField(max_length = 50, choices = TYPE,null = True, blank=True)
    def __str__(self):
        return self.title

class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='places/')


    def __str__(self):
        return self.name


class RoommsetImages(models.Model):
    roommset = models.ForeignKey(Roommset, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.property.title

class PropertyReview(models.Model):
    property = models.ForeignKey(Roommset, related_name='property_review', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='review_owner', on_delete=models.CASCADE)
    feedback = models.TextField(default='' , max_length=200)


    def __str__(self):
        return self.property.title
