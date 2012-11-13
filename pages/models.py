from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	key = models.IntegerField()

	def __unicode__(self):
		return self.title