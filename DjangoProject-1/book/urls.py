from django.urls import include,path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('publisher/', views.publisher, name="publisher")
]
