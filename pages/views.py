from django.http import HttpResponse
from django.shortcuts import render
from pages.models import Page

def homepage(request):

	return render(request, 'home.html')


def contacts(request):

	pages = Page.objects.all()

	return render(request, "contacts.html", {"pages": pages})