from django.db import models

from store.models import category
from .category import Category



# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.IntegerField(default=0)
	#here we are dding category model to the our product model
	category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
	
	descriptin = models.CharField(max_length=200 , default='' , null=True , blank=True)
	image = models.ImageField( upload_to = 'products/upload' )
	
	
	
	
	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in =ids)
	
	#Creating static method to get product.
	@staticmethod
	def get_all_products( ):
		return Product.objects.all()
	
	@staticmethod
	def get_all_products_by_categoryid (category_id) :
		if category_id:
			return Product.objects.filter(category = category_id)
		else:
			return Product.get_all_products();