from django.contrib import messages
from django.http import HttpResponseRedirect

# authentication
from django.shortcuts import redirect

from main_app.auth.auth_helper import get_access


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

    try:
        access_role = get_access(username, password)
        if (access_role):
            request.session['user_login'] = username
            request.session['role'] = access_role

            return redirect('status')

    except Exception as e:
        messages.error(request, "Username atau password salah")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def auth_logout(request):
    request.session.flush()

    return redirect('landing-page')
