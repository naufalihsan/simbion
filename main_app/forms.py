from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import TempatWawancara, SkemaBeasiswaAktif, Pendaftaran

class TempatWawancaraForm(forms.Form):
    kode = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'kode'}),
        label='Kode',
    )

    nama = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'nama tempat'}),
        label='Nama'
    )    

    lokasi = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'lokasi'}),
        label='Lokasi'
    )         

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        kode = self.cleaned_data['kode']

        is_exist_kode = "SELECT * FROM %s WHERE kode = '%s'" % (TempatWawancara._meta.db_table, kode)
        
        if len(list(TempatWawancara.objects.raw(is_exist_kode))) > 0:
            unique_kode_constraint_error = ValidationError(_('Tempat Wawancara with that kode already exists.'))
            self.add_error('kode', unique_kode_constraint_error)
            raise unique_kode_constraint_error

        return cleaned_data

class FormBeasiswaForm(forms.Form):

    kode_skema = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'kode_skema'}),
        label='Kode_skema',
    )

    IPK = forms.CharField( 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'IPK'}),
        label='IPK'
    )         

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        kode_skema = self.cleaned_data['kode_skema']

        is_exist_kode = "SELECT * FROM %s WHERE kode_skema_beasiswa = '%s'" % (SkemaBeasiswaAktif._meta.db_table, kode_skema)

        if len(list(SkemaBeasiswaAktif.objects.raw(is_exist_kode))) > 0:
            foreign_key_kode_constraint_error = ValidationError(_('Kode skema tidak ada.'))
            self.add_error('kode_skema', foreign_key_kode_constraint_error)
            raise foreign_key_kode_constraint_error

        return cleaned_data
