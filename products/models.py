from django.db import models


class Menu(models.Model):
	name 	= models.CharField(max_length=50)
	
	class Meta:
		db_table = 'menus'

class Category(models.Model):
	menu    = models.ForeignKey('Menu', on_delete=models.CASCADE)
	name	= models.CharField(max_length=50)
	

	class Meta:
		db_table = 'categories'

class Product(models.Model):
	category	= models.ForeignKey('Category', on_delete=models.CASCADE)
	korean_name	= models.CharField(max_length=50)
	english_name= models.CharField(max_length=50)
	description	= models.CharField(max_length=200)
	nutrition	= models.ForeignKey('Nutrition', on_delete=models.CASCADE)

	class Meta:
		db_table = 'products'

class Image(models.Model):
	image_url	= models.CharField(max_length=200)
	product		= models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'images'

class Nutrition(models.Model):
	one_serving_kacl= models.DecimalField(max_digits=8, decimal_places=2)
	sodium_mg		= models.DecimalField(max_digits=8, decimal_places=2)
	saturated_fat_g	= models.DecimalField(max_digits=8, decimal_places=2)
	sugars_g		= models.DecimalField(max_digits=8, decimal_places=2)
	protein_g		= models.DecimalField(max_digits=8, decimal_places=2)
	caffein_mg		= models.DecimalField(max_digits=8, decimal_places=2)
	size_ml			= models.CharField(max_length=50)
	size_fluid_ounce= models.CharField(max_length=50)

	class Meta:
		db_table = 'nutritions'

class Allergy(models.Model):
	name	= models.CharField(max_length=50)

	class Meta:
		db_table = 'allergies'

class Allergy_products(models.Model):
	allergy		= models.ForeignKey('Allergy', on_delete=models.CASCADE)
	product		= models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'al_products'





