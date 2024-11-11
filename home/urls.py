from django.urls import path
from . import views

urlpatterns = [
    #rota view index
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('ajuda', views.ajuda, name='ajuda'),
]