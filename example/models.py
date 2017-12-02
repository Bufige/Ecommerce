from django.db import models

# Create your models here.


class Products(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	imagePath = models.TextField()	
	description = models.TextField()
	price = models.FloatField()

	def __str__(self):
		return self.title