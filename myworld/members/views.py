from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

# Create your views here.
def index(request):
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['hobby']
  y = request.POST['beskriv']
  member = Members(hobby=x, beskrivelse=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  hobby = request.POST['hobby']
  beskriv = request.POST['beskriv']
  member = Members.objects.get(id=id)
  member.hobby = hobby
  member.beskrivelse = beskriv
  member.save()
  return HttpResponseRedirect(reverse('index'))



# https://www.w3schools.com/django/django_create_app.php