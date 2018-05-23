from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# from .views import kode_skema
from main_app.models import *


class daftarSkemaAktifForm(forms.Form):
    CHOICES = (('Prestasi', 'Prestasi'),('Tugas Akhir', 'Tugas Akhir'))


    no_urut = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'No_Urut'}),
        label='No Urut',
    )

    tgl_mulai_pendaftaran = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Tanggal Mulai Pendaftaran'}),
        label='Tanggal Mulai Pendaftaran',
    )

    tgl_tutup_pendaftaran = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Tanggal Tutup Pendaftaran'}),
        label='Tanggal Tutup Pendaftaran',
    )

    periode_penerimaan = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Periode Penerimaan'}),
        label='Periode Penerimaan',
    )

    status = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Status'}),
        label='Status',
    )

    jumlah_pendaftar = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Jumlah Pendaftar'}),
        label='Jumlah Pendaftar',
    )

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        kode = self.cleaned_data['kode']

        is_exist_kode = "SELECT * FROM %s WHERE kode = '%s'" % (SkemaBeasiswa._meta.db_table, kode)

        if len(list(SkemaBeasiswa.objects.raw(is_exist_kode))) > 0:
            unique_code_constraint_error = ValidationError(_('Schema with that code already exists.'))
            self.add_error('kode', unique_code_constraint_error)
            raise unique_code_constraint_error

        return cleaned_data
