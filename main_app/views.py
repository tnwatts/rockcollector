from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from main_app.models import Rock

# Create your views here.
def home(request):
  return render(request, 'home.html')

def what(request):
  return render(request, 'what.html')

def rocks_index(request):
  rocks = Rock.objects.all()
  return render(request, 'rocks/index.html', {'rocks' : rocks})

def rock_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  return render(request, 'rocks/detail.html', { 'rock': rock})

def rock_create(request, rock_id):
  rock = Rock.objects.create()
  return render(request, 'rocks/detail.html', { 'rock': rock})

class RockCreate(CreateView):
  model = Rock
  fields = '__all__'
  success_url = '/rocks/'     