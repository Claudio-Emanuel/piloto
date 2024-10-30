from . import views
from django.urls import path

urlpatterns = [
    #rota para view index
    path('index', views.index,name="index"),
]