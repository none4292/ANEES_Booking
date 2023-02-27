from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
GENDER = (
    ('male','male'),
    ('female','female'),
)

class Proflie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_proflie')
    gender = models.CharField(max_length=10, choices=GENDER)
    contact_number = models.CharField(max_length=12)
    address = models.CharField(max_length = 50)
    email = models.EmailField()
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
            Proflie.objects.create(user=instance)

