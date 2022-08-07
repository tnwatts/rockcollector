from django.shortcuts import render
from django.http import HttpResponse

class Rock:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, category, description, grams):
    self.name = name
    self.category = category
    self.description = description
    self.grams = grams

rocks = [
  Rock('Granny', 'Igneous', 'super old granite rock, set in her ways, stubborn but cares about the young rocks', 35),
  Rock('Rockette', 'Metamorphic', 'workhorse, used to be shale, now living the slate life, works hard and parties hard', 47),
  Rock('Carl', 'Sedimentary', 'very bland limestone rock, unstable personality, doesn\'t like other rocks', 22),
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def what(request):
    return render(request, 'what.html')

def rocks_index(request):
    return render(request, 'rocks/index.html', {'rocks' : rocks})