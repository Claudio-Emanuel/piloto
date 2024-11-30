from django.urls import path
from . import views

urlpatterns = [
    #rota view index
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('ajuda', views.ajuda, name='ajuda'),
    path('item/<int:id>',views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/',views.perfil, name='perfil'),
    path('diasemana/<int:num>',views.semana, name='semana'),
    path('produto', views.produto, name='produto'),
    path('produto/form', views.formproduto, name='formproduto'),
    path('produtos/detalhes/10', views.detalhes_produto, name='detalhes'),
    path('produtos/editar/10', views.formproduto, name='edit_produto'),
    path('produtos/excluir/10', views.excluir_produto, name='del_produto')
]