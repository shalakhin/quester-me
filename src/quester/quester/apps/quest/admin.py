from quest.models import *
from django.contrib.gis import admin

admin.site.register(Quest)
admin.site.register(Marker, admin.OSMGeoAdmin)
admin.site.register(Address)