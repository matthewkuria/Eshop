from django.db import models 
from django.contrib.auth.models import User
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	first_name = models.CharField(max_length=50) 
	last_name = models.CharField(max_length=50) 
	phone = models.CharField(max_length=10) 
	email = models.EmailField() 
	password = models.CharField(max_length=100) 

	def __str__(self):
    		return f"{self.first_name} {self.last_name}"

	# # to save the data 
	def register(self): 
		self.save()	
