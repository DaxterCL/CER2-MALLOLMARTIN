from django.urls import path

from . import views

urlpatterns = [
    # Públicas
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('lugar/<int:pk>/', views.detalle_lugar, name='detalle_lugar'),
    path('categorias/', views.lista_categorias, name='categorias'),
    path('categorias/<int:pk>/', views.lugares_por_categoria, name='lugares_por_categoria'),

    # Gestión (requieren sesión; agregar y editar además requieren permisos)
    path('gestion/', views.gestion, name='gestion'),
    path('gestion/lugar/nuevo/', views.crear_lugar, name='crear_lugar'),
    path('gestion/lugar/<int:pk>/editar/', views.editar_lugar, name='editar_lugar'),
]
