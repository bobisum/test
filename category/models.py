from django.db import models

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.category_name