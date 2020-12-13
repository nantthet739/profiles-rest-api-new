from django.contrib import admin

# Register your models here.

from profiles_api import models


#to be able to access from admin portal
admin.site.register(models.UserProfile)
