from notifications import services
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import os, os.path, json

# Create your views here.
def notifications(request):
	title = "Notification Center"

	args = { 'theTitle': title }

	if services.get():
		messages.info(request, services.get())
	return render(request, 'notifications.html', args)


# Create class + methods for each JSON data field

class getCount:
    def get():
        count = services.get()
        return render(request,'notifications.html', count)

