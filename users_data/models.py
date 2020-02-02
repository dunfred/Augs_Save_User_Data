from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(null=False, blank=False, max_length=255, unique=True)
    password = models.CharField(null=False, blank=False, max_length=255, unique=True)
    email    = models.EmailField(null=False, blank=False, max_length=255, unique=True)

    class Meta:
        verbose_name = "User Details" 
        
    def __str__(self):
        return self.username
    