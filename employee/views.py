from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

from .models import Employee

from .forms import EmployeeForm
from .forms import ContactEmergencyForm
from .forms import LiabilityForm


# Create your views here.

# Home
def home(request):
  return render(request, 'views/home.html')

# Terms
def terms(request):
  return render(request, 'views/terms.html')

# List workers
def workers(request):
  employees = Employee.objects.all()
  page = request.GET.get('page', 1)

  try:
    paginator = Paginator(employees, 5)
    employees = paginator.page(page)
  except:
    raise Http404

  print(employees)

  employeesData = {
    'entity': employees,
    'paginator': paginator
  }

  return render(request, 'workers/index.html', employeesData)

# Create workers
def workersCreate(request):
  form = EmployeeForm(request.POST or None, request.FILES or None)
  form2 = ContactEmergencyForm(request.POST or None, request.FILES or None)
  form3 = LiabilityForm(request.POST or None, request.FILES or None)

  formData = {
    'form': form,
    'form2': form2,
    'form3': form3,
  }

  if form.is_valid() and form2.is_valid() and form3.is_valid():
    form.save()  
    form2.save()
    form3.save()
    messages.success(request, "Trabajador creado correctamente")
    
    return redirect('workers')

  return render(request, 'workers/workerCreate.html', formData)

#
def workersUpdate(request, rut):
  employee = Employee.objects.get(employee_rut=rut)
  form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)
  #form2 = ContactEmergencyForm(request.POST or None, request.FILES or None, instance=employee)

  formData = {
    'form': form,
    # 'form2': form2
  }

  if form.is_valid() and request.POST:
    form.save()
    # form2.save()
    messages.success(request, "Trabajador editado correctamente")    

    return redirect('workers')

  return render(request, 'workers/workerUpdate.html', formData)

#
def workersDelete(request, rut):
  employee = Employee.objects.get(employee_rut=rut)
  employee.delete()
  messages.success(request, "Eliminado correctamente")    

  return redirect('workers')