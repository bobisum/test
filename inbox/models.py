from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	send_date = models.DateTimeField()
	title = models.CharField(max_length=150, blank=False)
	messege = models.TextField()
	read = models.BooleanField(default=False)
	sender = models.ForeignKey(User, related_name='message_sender')
	reciever = models.ForeignKey(User, related_name='message_reciever')

	def __unicode__(self):
		return self.title