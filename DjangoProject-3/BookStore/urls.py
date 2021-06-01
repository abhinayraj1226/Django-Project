from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registerAuthor', views.registerAuthor, name="registerAuthor"),
    path('registerPublisher', views.registerPublisher, name="registerPublisher"),
    path('publishBook', views.publishBook, name="publishBook"),
]
