from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate


def login_root(request):
    # Login form submitted?
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            # Login succeeded
            if user is not None:
                return HttpResponseRedirect(reverse('login.views.login_success'))

        # Login failed
        return HttpResponseRedirect(reverse('login.views.login_fail'))

    return render(request, 'login_root.html')


def login_success(request):
    return render(request, 'login_success.html')


def login_fail(request):
    return render(request, 'login_fail.html')
