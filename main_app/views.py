from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
import datetime
from main_app.utils.sqlizer import insert
from .forms import TempatWawancaraForm, FormBeasiswaForm
from .models import TempatWawancara, Pendaftaran, Mahasiswa, SkemaBeasiswaAktif

response = {}


def landing_page(request):
    return render(request, 'landingPage.html', response)


def login(request):
    return render(request, 'login.html', response)


def register(request):
    return render(request, 'register.html', response)


def register_donor(request):
    return render(request, 'registerDonor.html', response)


def status_login(request):
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return HttpResponseRedirect('login')


def dashboard(request):
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    session_data(response, request)

    if (response['role'] == 'mahasiswa'):
        return render(request, 'dashboardStudent.html', response)
    elif (response['role'] == 'donatur'):
        return render(request, 'dashboardDonor.html', response)
    elif (response['role'] == 'admin'):
        return render(request, 'dashboardAdmin.html', response)


def session_data(response, request):
    response['author'] = request.session['user_login']
    response['role'] = request.session['role']

def form_beasiswa(request):
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    if (request.session['role'] != 'mahasiswa'):
        return HttpResponseRedirect(reverse('dashboard'))

    response = {}
    obj = Mahasiswa.objects.filter(username=request.session.get('user_login'))

    if request.method == "POST":
        form = FormBeasiswaForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                new_pendaftaran = insert(table_name=Pendaftaran._meta.db_table,
                                        no_urut=Pendaftaran.objects.all().count(),
                                        kode_skema_beasiswa=form.cleaned_data['kode_skema'],
                                        npm=obj[0].npm,
                                        waktu_daftar=datetime.datetime.now(),
                                        status_daftar='daftar',
                                        status_terima='tidak aktif')
                cursor.execute(new_pendaftaran)
            response = {}
            response['status_daftar'] = 'berhasil mendaftar'
            response['form'] = TempatWawancaraForm()
            return render(request, 'tempat_wawancara.html', response)
        else:
            response['status_daftar'] = 'gagal mendaftar, kode skema tidak ada'
            response['loggedin'] = obj
            response['form'] = FormBeasiswaForm()
            return render(request, 'form_beasiswa.html', response)
    else:
        response['loggedin'] = obj
        response['form'] = FormBeasiswaForm()
        return render(request, 'form_beasiswa.html', response)

def tempat_wawancara(request):
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    if (request.session['role'] != 'admin'):
        return HttpResponseRedirect(reverse('dashboard'))

    if request.method == "POST":
        form = TempatWawancaraForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                new_tempat_wawancara = insert(table_name=TempatWawancara._meta.db_table,
                                        kode=form.cleaned_data['kode'],
                                        nama=form.cleaned_data['nama'],
                                        lokasi=form.cleaned_data['lokasi'])
                cursor.execute(new_tempat_wawancara)
            response = {}
            response['status_tempat'] = 'berhasil menambahkan data'
            response['form'] = TempatWawancaraForm()
            return render(request, 'tempat_wawancara.html', response)
        else:
            response = {}
            response['status_tempat'] = 'kode yang dimasukkan sudah eksis'
            response['form'] = TempatWawancaraForm()
            return render(request, 'tempat_wawancara.html', response)
    else:
        response = {}
        response['form'] = TempatWawancaraForm()
        return render(request, 'tempat_wawancara.html', response)

# # role : donatur
# # donatur mengecek list beasiswanya dia
# # tampilkan list beasiswa dia
# bisa di klik ke halaman baru buat liat detailnya, di /penerimaan_beasiswa
def list_beasiswa(request):
    return render(request, 'list_beasiswa.html', {})

def penerimaan_beasiswa(request):
    return render(request, 'list_beasiswa.html', {})
