from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'views/home.html')

def workers(request):
  return render(request, 'workers/index.html')

def workersCreate(request):
  return render(request, 'workers/workerCreate.html')

def workersUpdate(request):
  return render(request, 'workers/workerUpdate.html')