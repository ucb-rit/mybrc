from django.shortcuts import render, HttpResponse
from django.contrib import messages
from notifications.models import User
import os, os.path, json

# Create your views here.
def notifications(request):
	title = "Notification Center"
	args = { 'theTitle': title }
	send_notification(request)

	return render(request, 'notifications.html', args)

def send_notification(request):
	if request.method == "GET":
		usrBal = User.user_data[0]["UserBalance"]
		usrAlloc = User.user_data[0]["UserAllocation"]
		quotaRemaining = usrBal/usrAlloc

		if quotaRemaining < 0.01:
			return messages.info(request, "You've used up 100% of your quota")
		elif quotaRemaining < 0.1:
			return messages.info(request, "You've used up 90% of your quota")
		elif quotaRemaining < 0.25:
			return messages.info(request, "You've used up 75% of your quota")
		elif quotaRemaining < 0.5:
			return messages.info(request, "You've used up 50% of your quota")
