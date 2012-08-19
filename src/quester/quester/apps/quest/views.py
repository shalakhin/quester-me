import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr, GEOSGeometry

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
			"name": marker.quest.name,
			"desc": marker.quest.description,
			"type": marker.quest.get_type_display(),
			"level": marker.quest.get_difficulty_level_display(),
			"lat": marker.point.coords[0],
			"lon": marker.point.coords[1],
			"address": marker.address
		})
	return HttpResponse(json.dumps(response), mimetype='application/json')
