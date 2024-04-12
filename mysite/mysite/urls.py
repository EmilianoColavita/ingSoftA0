"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
"""








from django.contrib import admin
from django.urls import include, path
from polls import views  # Importa las vistas de la aplicación polls

urlpatterns = [
    path("", views.index, name="index"),  # Ruta raíz del sitio que apunta a la vista index de polls
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]


