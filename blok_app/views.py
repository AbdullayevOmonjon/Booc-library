from django.shortcuts import render,redirect
from .models import *
# from datetime import datetime

# Create your views here.
def home(request):
  return render(request,'home.html')

def maqola(request,son):
  data={
    'm1':Maqola.objects.filter(id=son),
  }
  return render(request,'maqola.html',data)

def blog(request):
  data={
    "m":Maqola.objects.all()
  }
  return render(request,'blog.html',data)


def about(request):
  return render(request,'about.html')
