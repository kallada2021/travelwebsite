from django.contrib import admin

from .models import UserProfile, Booking

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Booking)