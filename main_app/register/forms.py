from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from main_app.models import Pengguna, Mahasiswa, Donatur, IndividualDonor, Yayasan


class RegistrasiUserForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'username'}),
        label='Username',
    )

    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'validate',
                'placeholder': 'password',
            }),
        label='Password'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'validate', 'placeholder': 'email@example.com'}),
        label='Email'
    )

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        username = self.cleaned_data['username']

        is_exist_username = "SELECT * FROM %s WHERE username = '%s'" % (Pengguna._meta.db_table, username)

        if len(list(Pengguna.objects.raw(is_exist_username))) > 0:
            unique_username_constraint_error = ValidationError(_('User with that username already exists.'))
            self.add_error('username', unique_username_constraint_error)
            raise unique_username_constraint_error

        password = self.cleaned_data['password']

        if len(password) < 8:
            password_min_length = ValidationError(_('Password length min 8 character.'))
            self.add_error('password', password_min_length)
            raise password_min_length

        return cleaned_data


class RegistrasiMahasiswaForm(RegistrasiUserForm):
    npm = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'NPM'}),
        label='NPM'
    )

    nama = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'nama lengkap'}),
        label='Nama Lengkap'
    )

    no_telp = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'pattern': "^+62[0-9]{9,}$",
            'placeholder': 'no telp (+62)',
        })
    )
    alamat_tinggal = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'alamat'}),
        label='Alamat Tinggal'
    )

    alamat_domisili = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'alamat'}),
        label='Alamat Domisili'
    )

    nama_bank = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'nama bank'}),
        label='Nama Bank'
    )

    no_rekening = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'pattern': "^[0-9]{9,}$",
            'placeholder': 'no rekening',
        })
    )

    nama_pemilik = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'nama pemilik'}),
        label='Nama Pemilik'
    )

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        npm = self.cleaned_data['npm']

        is_exist_npm = "SELECT * FROM %s WHERE npm = '%s'" % (Mahasiswa._meta.db_table, npm)

        if len(list(Mahasiswa.objects.raw(is_exist_npm))) > 0:
            unique_npm_constraint_error = ValidationError(_('User with that npm already exists.'))
            self.add_error('npm', unique_npm_constraint_error)
            raise unique_npm_constraint_error

        return cleaned_data


class RegistrasiDonaturForm(RegistrasiUserForm):
    nomor_identitas = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Nomor identitas'}),
        label='Nomor Identitas'
    )

    npwp = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'NPWP'}),
        label='NPWP'
    )

    no_telp = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'pattern': "^+62[0-9]{9,}$",
            'placeholder': 'no telp (+62)',
        })
    )

    alamat = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'alamat'}),
        label='Alamat'
    )

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        nomor_identitas = self.cleaned_data['nomor_identitas']

        is_exist_identitas = "SELECT * FROM %s WHERE nomor_identitas = '%s'" % (Donatur._meta.db_table, nomor_identitas)

        if len(list(Donatur.objects.raw(is_exist_identitas))) > 0:
            unique_identitas_constraint_error = ValidationError(_('User with that nomor identitas already exists.'))
            self.add_error('nomor_identitas', unique_identitas_constraint_error)
            raise unique_identitas_constraint_error

        return cleaned_data


class RegistrasiIndividualDonor(RegistrasiDonaturForm):
    nama_lengkap = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'nama lengkap'}),
        label='Nama Lengkap'
    )

    nik = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'NIK'}),
        label='NIK'
    )


    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        nik = self.cleaned_data['nik']

        if len(nik) != 16:
            nik_min_length = ValidationError(_('NIK length must exactly 16 character.'))
            self.add_error('nik', nik_min_length)
            raise nik_min_length


        is_exist_nik = "SELECT * FROM %s WHERE nik = '%s'" % (IndividualDonor._meta.db_table, nik)

        if len(list(IndividualDonor.objects.raw(is_exist_nik))) > 0:
            unique_nik_constraint_error = ValidationError(_('User with that nik already exists.'))
            self.add_error('nik', unique_nik_constraint_error)
            raise unique_nik_constraint_error

        return cleaned_data


class RegistrasiYayasan(RegistrasiDonaturForm):
    nama_yayasan = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'nama yayasan'}),
        label='Nama Yayasan'
    )
    no_sk_yayasan = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'no sk yayasan'}),
        label='Nomor SK Yayasan'
    )

    no_telp_cp = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'pattern': "^+62[0-9]{9,}$",
            'placeholder': 'no telp cp',
        })
    )

    def clean(self):
        super().clean()

        cleaned_data = self.cleaned_data

        no_sk_yayasan = self.cleaned_data['no_sk_yayasan']

        is_exist_yayasan = "SELECT * FROM %s WHERE no_sk_yayasan = '%s'" % (Yayasan._meta.db_table, no_sk_yayasan)

        if len(list(Yayasan.objects.raw(is_exist_yayasan))) > 0:
            unique_yayasan_constraint_error = ValidationError(_('User with that no yayasan already exists.'))
            self.add_error('no_sk_yayasan', unique_yayasan_constraint_error)
            raise unique_yayasan_constraint_error

        return cleaned_data
