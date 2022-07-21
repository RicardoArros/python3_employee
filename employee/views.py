from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse("<h1>Bienvenido a Colaboradores Yuri</h1>")

def workers(request):
  return render(request, 'workers/index.html')

def aboutUs(request):
  return render(request, 'views/about-us.html')