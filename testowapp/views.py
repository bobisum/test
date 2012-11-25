from django.http import HttpResponse
from django.shortcuts import render
from testowapp.models import Avtomobili

def avtomobili(request):

	avtomobili = Avtomobili.objects.all()

	return render(request, "testow.html", {"avtomobili": avtomobili})