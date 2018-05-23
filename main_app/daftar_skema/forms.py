from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from main_app.models import *


class daftarSkemaForm(forms.Form):
    CHOICES = (('Prestasi', 'Prestasi'), ('Ekonomi', 'Ekonomi'), ('Tugas Akhir', 'Tugas Akhir'))
    kode = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Kode'}),
        label='Kode',
    )

    nama = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Nama'}),
        label='Nama',
    )

    jenis = forms.ChoiceField(choices=CHOICES,
                              widget=forms.Select(attrs={'class': 'validate', 'placeholder': 'Jenis'}),
                              required=True)

    deskripsi = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Deskripsi'}),
        label='Deskripsi',
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


