from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout


def home(request):
    """
        Handle main page stuff
    """

    return render(request, 'defaults/home.html')


def logout(request):
    """
        Logout the user
    """

    django_logout(request)
    return redirect('home')
