from django.db import models

class Message(models.Model):
	send_date = models.DateTimeField()
	title = models.CharField(max_length=150, blank=False)
	messege = models.TextField()
	read = models.BooleanField(default=False)
	sender = models.ForeignKey('User')
	reciever = models.ForeignKey('User')

	def __unicode__(self):
		return self.title