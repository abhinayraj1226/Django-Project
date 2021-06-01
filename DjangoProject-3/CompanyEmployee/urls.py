from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('addEmployee', views.addEmployee, name = "addEmployee"),
    path('findEmployee', views.findEmployee, name="findEmployee")
]
