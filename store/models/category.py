from django.db import models 


class Category(models.Model): 
	name = models.CharField(max_length=13) 

	@staticmethod
	def get_all_categories(): 
		return Category.objects.all() 

	def __str__(self): 
		return self.name 
