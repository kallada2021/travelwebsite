from django.db import models
from django.urls import reverse


class Destination(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Destinations"
        ordering = ("created_at",)

    def get_absolute_url(self):
        return reverse("destination-single", args=[self.city])

    def __str__(self) -> str:
        return f"{self.country} + {self.city}"
    

class Tour(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Tours"
        ordering = ("created_at",)
        
    def get_absolute_url(self):
        return reverse("tour-single", args=[self.name])
    
    def __str__(self) -> str:
        return f"{self.name} + {self.destination}"
    
