"""simbion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main_app.auth.auth import auth_login, auth_logout
from main_app.views import landing_page, login, dashboard, status_login, register, register_donor, form_beasiswa, tempat_wawancara, list_beasiswa, penerimaan_beasiswa

from main_app.register.urls import urlpatterns as register_urls
from main_app.daftar_skema.urls import urlpatterns as daftar_skema_urls
from main_app.daftar_skema_aktif.urls import urlpatterns as daftar_skema_aktif_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landing_page, name='landing-page'),    

    path('login/', login, name='login'),

    path('register/', register, name='register'),
    path('register/donor/', register_donor, name='register-donor'),

    path('auth_login/', auth_login, name='login-auth'),
    path('auth_logout/', auth_logout, name='logout-auth'),

    path('status/', status_login, name='status'),

    path('dashboard/', dashboard, name='dashboard'),

    path('form_beasiswa/', form_beasiswa, name='form-beasiswa'),

    path('tempat_wawancara/', tempat_wawancara, name='tempat-wawancara'),

    path('list_beasiswa/', list_beasiswa, name='list-beasiswa'),

    path('penerimaan_beasiswa/', penerimaan_beasiswa, name='penerimaan-beasiswa'),

    *daftar_skema_urls,
    *daftar_skema_aktif_urls,
    *register_urls,


]
