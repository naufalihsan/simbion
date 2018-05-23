from django.urls import path

from main_app.daftar_skema_aktif.views import daftar_skema_aktif

urlpatterns = [
    path('daftar/beasiswa-aktif/', daftar_skema_aktif, name="daftar-skema"),
]
