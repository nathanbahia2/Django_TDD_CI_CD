from django.urls import path

from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.cadastrar_e_editar_contato, name='cadastrar_contato'),
    path('editar/<int:pk>', views.cadastrar_e_editar_contato, name='editar_contato'),
    path('excluir/<int:pk>', views.excluir_contato, name='excluir_contato'),
]
