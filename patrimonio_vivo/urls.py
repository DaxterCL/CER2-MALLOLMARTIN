from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inicio y cierre de sesión usan las vistas que ya trae Django
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # El resto de las rutas están en la app "catalogo"
    path('', include('catalogo.urls')),
]
