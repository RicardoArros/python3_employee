from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def home(request):
  return render(request, 'views/home.html')


def workers(request):
  employees = Employee.objects.all()

  print(employees)

  return render(request, 'workers/index.html', {'employees': employees})


def workersCreate(request):
  return render(request, 'workers/workerCreate.html')


def workersUpdate(request):
  return render(request, 'workers/workerUpdate.html')