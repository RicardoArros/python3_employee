from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Employee

from .forms import EmployeeForm


# Create your views here.

def home(request):
  return render(request, 'views/home.html')


def workers(request):
  employees = Employee.objects.all()

  print(employees)

  return render(request, 'workers/index.html', {'employees': employees})


def workersCreate(request):
  form = EmployeeForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('workers')


  return render(request, 'workers/workerCreate.html', {'form': form})


def workersUpdate(request):
  return render(request, 'workers/workerUpdate.html')