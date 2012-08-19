import json
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr, GEOSGeometry
from django.template import loader
from django.template.context import Context, RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect

from quest.models import Quest, Marker


def nearest_quests(request):
    if not request.is_ajax():
        return HttpResponseBadRequest("Must be AJAX")
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    distance = request.GET.get('distance')
    if not lat or not lon:
        return HttpResponseBadRequest("lat and lon must be provided")
    u_location = fromstr('POINT(%s %s)' % (lat, lon))
    marker_list = Marker.objects.filter(point__distance_lte=(u_location, D(km=distance or 1)))
    response = []
    for marker in marker_list:
        response.append({
            "quest_id": marker.quest.id,
            "marker_id": marker.id,
            "name": marker.quest.name,
            "desc": marker.quest.description,
            "type": marker.quest.get_type_display(),
            "level": marker.quest.get_difficulty_level_display(),
            "lat": marker.point.coords[0],
            "lon": marker.point.coords[1],
            "address": marker.address
        })
    return HttpResponse(json.dumps(response), mimetype='application/json')

def marker_fullinfo(request):
    if not request.is_ajax():
        return HttpResponseBadRequest("Must be AJAX")
    marker_id = request.GET.get("marker_id")
    if not marker_id:
        return HttpResponseBadRequest("Marker id MUST be provided")
    try:
        marker = Marker.objects.get(id=int(marker_id))
    except Marker.DoesNotExist:
        return HttpResponse("Something goes wrong")
    data = {
        "marker": marker
    }
    return HttpResponse(render_to_string("quest/marker_fullinfo.html", data))

from quest.forms import QuestForm

@ csrf_protect
def quest_form(request):


    f = QuestForm(request.POST or None)

    if request.method == 'POST':
        if f.is_valid():
            f.save()
            return redirect(reverse('home'))
        else:
            print 'here'

    f = QuestForm()
    c = RequestContext(request, {
        'f': f,
    })
    t = loader.get_template('quest/quest_form.html')
    html = t.render(Context(c))
    data = {'html': html, 'success': True}



    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')
