from django.urls import path

from main_app.daftar_skema.views import daftar_skema

urlpatterns = [
    path('daftar/skema/', daftar_skema, name="daftar-skema"),
]
