from django.db import models


class Admin(models.Model):
    username = models.ForeignKey('Pengguna', models.DO_NOTHING, db_column='username', primary_key=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Donatur(models.Model):
    nomor_identitas = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    npwp = models.CharField(max_length=20)
    no_telp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    username = models.ForeignKey('Pengguna', models.DO_NOTHING, db_column='username')

    class Meta:
        managed = False
class Donatur(models.Model):
    nomor_identitas = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    npwp = models.CharField(max_length=20)
    no_telp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    username = models.ForeignKey('Pengguna', models.DO_NOTHING, db_column='username')

    class Meta:
        managed = False
        db_table = 'donatur'


class IndividualDonor(models.Model):
    nik = models.CharField(primary_key=True, max_length=16)
    nomor_identitas_donatur = models.ForeignKey(Donatur, models.DO_NOTHING, db_column='nomor_identitas_donatur')

    class Meta:
        managed = False
        db_table = 'individual_donor'


class Mahasiswa(models.Model):
    npm = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    no_telp = models.CharField(max_length=20, blank=True, null=True)
    alamat_tinggal = models.CharField(max_length=50)
    alamat_domisili = models.CharField(max_length=50)
    nama_bank = models.CharField(max_length=50)
    no_rekening = models.CharField(max_length=20)
    nama_pemilik = models.CharField(max_length=20)
    username = models.ForeignKey('Pengguna', models.DO_NOTHING, db_column='username')

    class Meta:
        managed = False
        db_table = 'mahasiswa'


class Pembayaran(models.Model):
    urutan = models.IntegerField(primary_key=True)
    kode_skema_beasiswa = models.ForeignKey('SkemaBeasiswaAktif', models.DO_NOTHING, db_column='kode_skema_beasiswa')
    no_urut_skema_beasiswa_aktif = models.IntegerField()
    npm = models.ForeignKey(Mahasiswa, models.DO_NOTHING, db_column='npm')
    tgl_bayar = models.DateField()
    nominal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pembayaran'
        unique_together = (('urutan', 'kode_skema_beasiswa', 'no_urut_skema_beasiswa_aktif', 'npm'),)


class Pendaftaran(models.Model):
    no_urut = models.IntegerField(primary_key=True)
    kode_skema_beasiswa = models.ForeignKey('SkemaBeasiswaAktif', models.DO_NOTHING, db_column='kode_skema_beasiswa')
    npm = models.ForeignKey(Mahasiswa, models.DO_NOTHING, db_column='npm')
    waktu_daftar = models.DateTimeField()
    status_daftar = models.CharField(max_length=20)
    status_terima = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pendaftaran'
        unique_together = (('no_urut', 'kode_skema_beasiswa', 'npm'),)


class Pengguna(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pengguna'


class Pengumuman(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_urut_skema_beasiswa_aktif = models.IntegerField()
    kode_skema_beasiswa = models.ForeignKey('SkemaBeasiswaAktif', models.DO_NOTHING, db_column='kode_skema_beasiswa')
    username = models.ForeignKey(Pengguna, models.DO_NOTHING, db_column='username')
    judul = models.CharField(max_length=20)
    isi = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'pengumuman'
        unique_together = (('tanggal', 'no_urut_skema_beasiswa_aktif', 'kode_skema_beasiswa', 'username'),)


class RiwayatAkademik(models.Model):
    no_urut = models.IntegerField(primary_key=True)
    npm = models.ForeignKey(Mahasiswa, models.DO_NOTHING, db_column='npm')
    semester = models.CharField(max_length=1)
    tahun_ajaran = models.CharField(max_length=9)
    jumlah_sks = models.IntegerField()
    ips = models.FloatField()
    lampiran = models.CharField(max_length=50)
    no_rekening = models.CharField(max_length=20)
    nama_pemilik = models.CharField(max_length=20)
    username = models.ForeignKey(Pengguna, models.DO_NOTHING, db_column='username')

    class Meta:
        managed = False
        db_table = 'riwayat_akademik'
        unique_together = (('no_urut', 'npm'),)


class SkemaBeasiswa(models.Model):
    kode = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=50)
    jenis = models.CharField(max_length=20)
    deskripsi = models.CharField(max_length=50)
    nomor_identitas_donatur = models.ForeignKey(Donatur, models.DO_NOTHING, db_column='nomor_identitas_donatur')

    class Meta:
        managed = False
        db_table = 'skema_beasiswa'


class SkemaBeasiswaAktif(models.Model):
    kode_skema_beasiswa = models.ForeignKey(SkemaBeasiswa, models.DO_NOTHING, db_column='kode_skema_beasiswa', primary_key=True)
    no_urut = models.IntegerField()
    tgl_mulai_pendaftaran = models.DateField()
    tgl_tutup_pendaftaran = models.DateField()
    periode_penerimaan = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    jumlah_pendaftar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skema_beasiswa_aktif'
        unique_together = (('kode_skema_beasiswa', 'no_urut'),)


class SyaratBeasiswa(models.Model):
    kode_beasiswa = models.ForeignKey(SkemaBeasiswa, models.DO_NOTHING, db_column='kode_beasiswa', primary_key=True)
    syarat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'syarat_beasiswa'
        unique_together = (('kode_beasiswa', 'syarat'),)


class TempatWawancara(models.Model):
    kode = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tempat_wawancara'


class Wawancara(models.Model):
    no_urut_skema_beasiswa_aktif = models.IntegerField(primary_key=True)
    kode_skema_beasiswa = models.ForeignKey(SkemaBeasiswaAktif, models.DO_NOTHING, db_column='kode_skema_beasiswa')
    jadwal = models.DateTimeField()
    kode_tempat_wawancara = models.ForeignKey(TempatWawancara, models.DO_NOTHING, db_column='kode_tempat_wawancara')

    class Meta:
        managed = False
        db_table = 'wawancara'
        unique_together = (('no_urut_skema_beasiswa_aktif', 'kode_skema_beasiswa', 'jadwal'),)


class Yayasan(models.Model):
    no_sk_yayasan = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    no_telp_cp = models.CharField(max_length=20, blank=True, null=True)
    nomor_identitas_donatur = models.ForeignKey(Donatur, models.DO_NOTHING, db_column='nomor_identitas_donatur', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yayasan'
