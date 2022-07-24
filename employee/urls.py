from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('', views.home, name='home'),
  path('workers', views.workers, name='workers'),
  path('workers/create', views.workersCreate, name='workerCreate'),
  path('workers/update', views.workersUpdate, name='workerUpdate'),
  path('delete/<str:rut>', views.workersDelete, name='workerDelete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)