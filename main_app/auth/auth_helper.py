from django.db import connection

from main_app.models import Pengguna


def get_access(username, password):
    try:
        user = Pengguna.objects.raw(
            "SELECT * FROM %s WHERE username = '%s'" % (Pengguna._meta.db_table, username))[0]

        if (user.password == password):
            return user.role

    except Exception as e:
        raise Exception("username atau password salah, input : [{}, {}]".format(username, password))
