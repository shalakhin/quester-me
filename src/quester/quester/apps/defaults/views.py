from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout


def home(request):
    """
        Handle main page stuff
    """
    c = dict()
    #TODO: get actual user location if it possible using UserLocation model

    return render(request, 'defaults/home.html')


def logout(request):
    """
        Logout the user
    """

    django_logout(request)
    return redirect('home')

def get_user_location(request):
    user_location = request.user.user_location
    print user_location
