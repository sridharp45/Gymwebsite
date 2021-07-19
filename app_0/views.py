from django.shortcuts import render,HttpResponse
from datetime import datetime
from app_0.models import Contact
# Create your views here.
def index(request):
 return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def services(request):
  return HttpResponse('here our services for you')
def contacts(request):
  return HttpResponse('contact us through')
def dietplan(request):
  return render(request,'diet.html')
def workoutplan(request):
  return render(request,'workout.html')
def contact(request):
    if request.method=="POST":
      Name=request.POST.get('name')
      email=request.POST.get('email')
      text=request.POST.get('text')
      date=request.POST.get('date')
      contact=Contact(Name=Name, email=email, text=text, date=datetime.today())
      contact.save()
    return render(request,'contact.html')
