from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.gis.measure import D
from django.contrib.gis.geos import *

from quest.models import Quest, Marker, QUEST_CHOICES

def home(request):
    """
        Handle main page stuff
    """
    c = dict()
    #TODO: get actual user location if it possible using UserLocation model


    pnt = fromstr('POINT(%s %s)' % (str(request.LOCATION_DATA['longitude']), str(request.LOCATION_DATA['latitude'])), srid=4326)
    markers = Marker.objects.filter(point__distance_lte=(pnt, D(km=10))).geojson()
    c['markers'] = markers

    c['quest_choices'] = QUEST_CHOICES
    print c['quest_choices']

    return render(request, 'defaults/home.html', c)


def logout(request):
    """
        Logout the user
    """

    django_logout(request)
    return redirect('home')

def get_user_location(request):
    pass

def set_user_location(request):
    pass