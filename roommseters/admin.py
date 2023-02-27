from django.contrib import admin
from .models import Roommset , RoommsetImages , Place , PropertyReview 
# Register your models here.
admin.site.register([Roommset])
admin.site.register([RoommsetImages])
admin.site.register([Place])
admin.site.register([PropertyReview])