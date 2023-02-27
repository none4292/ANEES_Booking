from django.db import models

# Create your models here.
class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goal = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')
    why_choose_us =  models.TextField(max_length=1000)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.what_we_do
