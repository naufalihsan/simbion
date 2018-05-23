from django.urls import path

from main_app.register.views import registrasi_mahasiswa, registrasi_individual_donor, registrasi_yayasan

urlpatterns = [
    path('register/student/', registrasi_mahasiswa, name="register-student"),
    path('register/individual/', registrasi_individual_donor, name="register-individual"),
    path('register/yayasan/', registrasi_yayasan, name="register-yayasan"),
]
