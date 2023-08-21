from django.shortcuts import render
from .models import Message

# Create your views here.
def index(request):
  return render(request, 'contact-form.html')

def addmessage(request):

  name = request.POST['name']
  email = request.POST['email']
  subject = request.POST['subject']
  message = request.POST['message']
  messageContent = Message(name=name, email=email, subject=subject, message=message)

  try:
    messageContent.save()
    context = {
      'isSuccessfull': True,
    }
  except:
    context = {
      'isSuccessfull': False,
    }
  return render(request, "confirmation.html", context)