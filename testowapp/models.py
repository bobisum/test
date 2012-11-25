from django.db import models

class Avtomobili(models.Model):
	marka = models.CharField(max_length=30)
	model = models.CharField(max_length=30)

	def __unicode__(self):
		return self.marka + ' ' + self.model