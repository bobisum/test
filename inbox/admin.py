from django.contrib import admin
from inbox.models import Message

class MessagesAdmin(admin.ModelAdmin):
	pass
admin.site.register(Message, MessagesAdmin)