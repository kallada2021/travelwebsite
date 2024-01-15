import uuid
from django.db import models
from django.contrib.auth.models import User
from main.models import Tour


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "User Profiles"
        ordering = ("created_at",)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    
class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_paid = models.BooleanField(default=False)
    traveller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Bookings"
        ordering = ("created_at",)
    
    def __str__(self) -> str:
        return f"{self.booking_id}"