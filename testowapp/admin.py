from django.contrib import admin
from testowapp.models import Avtomobili

class TestowappAdmin(admin.ModelAdmin):
	pass
admin.site.register(Avtomobili, TestowappAdmin)