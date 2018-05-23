from django.db import connection

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

from main_app.auth.auth_helper import get_access
from main_app.models import Pengguna, Mahasiswa, IndividualDonor, Donatur, Yayasan
from main_app.utils.sqlizer import insert

from .forms import RegistrasiMahasiswaForm, RegistrasiYayasan, RegistrasiIndividualDonor


@require_http_methods(["GET", "POST"])
def registrasi_mahasiswa(request):
    if request.method == "POST":
        form = RegistrasiMahasiswaForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                new_pengguna = insert(table_name=Pengguna._meta.db_table,
                                      username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      role='mahasiswa')

                new_mahasiswa = insert(table_name=Mahasiswa._meta.db_table,
                                       npm=form.cleaned_data['npm'],
                                       email=form.cleaned_data['email'],
                                       nama=form.cleaned_data['nama'],
                                       no_telp=form.cleaned_data['no_telp'],
                                       alamat_tinggal=form.cleaned_data['alamat_tinggal'],
                                       alamat_domisili=form.cleaned_data['alamat_domisili'],
                                       nama_bank=form.cleaned_data['nama_bank'],
                                       no_rekening=form.cleaned_data['no_rekening'],
                                       nama_pemilik=form.cleaned_data['nama_pemilik'],
                                       username=form.cleaned_data['username'])

                cursor.execute(new_pengguna)
                cursor.execute(new_mahasiswa)

            access_role = get_access(form.cleaned_data['username'], form.cleaned_data['password'])

            if (access_role):
                request.session['user_login'] = form.cleaned_data['username']
                request.session['role'] = access_role

                return redirect('status')

    else:
        form = RegistrasiMahasiswaForm()

    return render(request, 'registerStudent.html', {'form': form})


@require_http_methods(["GET", "POST"])
def registrasi_individual_donor(request):
    if request.method == "POST":
        form = RegistrasiIndividualDonor(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                new_pengguna = insert(table_name=Pengguna._meta.db_table,
                                      username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      role='donatur')

                new_donatur = insert(table_name=Donatur._meta.db_table,
                                     nomor_identitas=form.cleaned_data['nomor_identitas'],
                                     email=form.cleaned_data['email'],
                                     nama=form.cleaned_data['nama_lengkap'],
                                     npwp=form.cleaned_data['npwp'],
                                     no_telp=form.cleaned_data['no_telp'],
                                     alamat=form.cleaned_data['alamat'],
                                     username=form.cleaned_data['username'])

                new_individual_donor = insert(table_name=IndividualDonor._meta.db_table,
                                              nik=form.cleaned_data['nik'],
                                              nomor_identitas_donatur=form.cleaned_data['nomor_identitas'])

                cursor.execute(new_pengguna)
                cursor.execute(new_donatur)
                cursor.execute(new_individual_donor)

            access_role = get_access(form.cleaned_data['username'], form.cleaned_data['password'])

            if (access_role):
                request.session['user_login'] = form.cleaned_data['username']
                request.session['role'] = access_role

                return redirect('status')

    else:
        form = RegistrasiIndividualDonor()

    return render(request, 'registerIndividual.html', {'form': form})


@require_http_methods(["GET", "POST"])
def registrasi_yayasan(request):
    if request.method == "POST":
        form = RegistrasiYayasan(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                new_pengguna = insert(table_name=Pengguna._meta.db_table,
                                      username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      role='donatur')

                new_donatur = insert(table_name=Donatur._meta.db_table,
                                     nomor_identitas=form.cleaned_data['nomor_identitas'],
                                     email=form.cleaned_data['email'],
                                     nama=form.cleaned_data['nama_yayasan'],
                                     npwp=form.cleaned_data['npwp'],
                                     no_telp=form.cleaned_data['no_telp'],
                                     alamat=form.cleaned_data['alamat'],
                                     username=form.cleaned_data['username'])

                new_yayasan = insert(table_name=Yayasan._meta.db_table,
                                     no_sk_yayasan=form.cleaned_data['no_sk_yayasan'],
                                     email=form.cleaned_data['email'],
                                     nama=form.cleaned_data['nama_yayasan'],
                                     no_telp_cp=form.cleaned_data['no_telp'],
                                     nomor_identitas_donatur=form.cleaned_data['nomor_identitas'])

                cursor.execute(new_pengguna)
                cursor.execute(new_donatur)
                cursor.execute(new_yayasan)

            access_role = get_access(form.cleaned_data['username'], form.cleaned_data['password'])

            if (access_role):
                request.session['user_login'] = form.cleaned_data['username']
                request.session['role'] = access_role

                return redirect('status')

    else:
        form = RegistrasiYayasan()

    return render(request, 'registerYayasan.html', {'form': form})
