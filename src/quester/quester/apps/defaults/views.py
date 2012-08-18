from django.shortcuts import render


def home(request):
    """
        Handle main page stuff
    """

    return render(request, 'defaults/home.html')
