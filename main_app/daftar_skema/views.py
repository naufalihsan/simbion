from django.db import connection

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

from main_app.auth.auth_helper import get_access
from main_app.models import *
from main_app.utils.sqlizer import insert

from .forms import daftarSkemaForm


@require_http_methods(["GET", "POST"])
def daftar_skema(request):
    if request.method == "POST":
        form = daftarSkemaForm(request.POST)
        if form.is_valid():
            donatur = Donatur.objects.get(username=request.session.get('user_login'))
            nomor_identitas_donatur = donatur.nomor_identitas
            with connection.cursor() as cursor:
                new_skemaBeasiswa = insert(table_name=SkemaBeasiswa._meta.db_table,
                                           kode=form.cleaned_data['kode'],
                                           nama=form.cleaned_data['nama'],
                                           jenis=form.cleaned_data['jenis'],
                                           deskripsi=form.cleaned_data['deskripsi'],
                                           nomor_identitas_donatur=nomor_identitas_donatur
                                           )

                # new_skemaBeasiswaAktif = insert(table_name=SkemaBeasiswaAktif._meta.db_table,
                #                                 kode_skema_beasiswa=form.cleaned_data['kode_skema_beasiswa'],
                #                                 no_urut=form.cleaned_data['no_urut'],
                #                                 tgl_mulai_pendaftaran=form.cleaned_data['tgl_mulai_pendaftaran'],
                #                                 tgl_tutup_pendaftaran=form.cleaned_data['tgl_tutup_pendaftaran'],
                #                                 periode_penerimaan=form.cleaned_data['periode_penerimaan'],
                #                                 status=form.cleaned_data['status'],
                #                                 jumlah_pendaftar=form.cleaned_data['jumlah_pendaftar'])

                cursor.execute(new_skemaBeasiswa)
                # cursor.execute(new_skemaBeasiswaAktif)



    else:
        form = daftarSkemaForm()

    return render(request, 'daftar_skema.html', {'form': form})
