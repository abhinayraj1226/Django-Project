from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:cname>', views.page, name="page")
]
