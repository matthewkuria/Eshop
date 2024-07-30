from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)
