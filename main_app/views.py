from sre_constants import CATEGORY_UNI_DIGIT
from secrets import token_bytes
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CleaningForm
import uuid
import boto3
from .models import Rock,Dirt, Photo
import os
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
  cleaning_form = CleaningForm()
  dirt_ids = rock.dirt.all().values_list('id')
  dirt = Dirt.objects.exclude(id__in=dirt_ids)
  return render(request, 'rocks/detail.html', { 'rock': rock, 'cleaning_form': cleaning_form, 'dirt': dirt })


class RockCreate(CreateView):
  model = Rock
  fields = '__all__'
  success_url = '/rocks/'     

class RockUpdate(UpdateView):
  model = Rock
  fields = ['category','description', 'grams']

class RockDelete(DeleteView):
  model = Rock
  success_url = '/rocks/'   
  

def add_cleaning(request, rock_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning= form.save(commit=False)
    new_cleaning.rock_id = rock_id
    new_cleaning.save()
  return redirect('detail', rock_id=rock_id)


class DirtList(ListView):
  model = Dirt


class DirtList(DetailView):
  model = Dirt


class DirtList(CreateView):
  model = Dirt
  fields = '__all__'


class DirtList(UpdateView):
  model = Dirt
  fields = ['name', 'color']


class DirtList(DeleteView):
  model = Dirt
  success_url = '/toys/'

def assoc_dirt(request, rock_id, dirt_id):
  rock = Rock.objects.get(id=rock_id)
  rock.dirt.add(dirt_id)
  return redirect('detail', rock_id=rock_id)

def unassoc_dirt(request,rock_id, dirt_id):
  rock = Rock.objects.get(id=rock_id)
  rock.dirt.remove(rock_id)
  return redirect('detail', rock_id=rock_id)

def add_photo(request, rock_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)

  if photo_file:
      s3 = boto3.client('s3')
      # need a unique "key" for S3 / needs image file extension too
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      # just in case something goes wrong
      try:
          print(os.environ)
          bucket = os.environ['S3_BUCKET']
          s3.upload_fileobj(photo_file, bucket, key)
          # build the full url string
          url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
          Photo.objects.create(url=url, rock_id=rock_id)
      except Exception as e:
          print('An error occurred uploading file to S3')
          print(e)
  return redirect('detail', rock_id=rock_id)

