from django.contrib.gis.utils import GeoIP
from django.conf import settings

class InitializeMiddleware(object):

    """
    A simple middleware component that allow
    to detect user geo data by ip address
    """

    def process_request(self, request):

        request.LOCATION_DATA = False
        ip = request.META.get('HTTP_X_FORWARDED_FOR', '')\
            or request.META.get('HTTP_X_REAL_IP', '')\
            or request.META.get('REMOTE_ADDR', '')

        if ip:
            g = GeoIP()
            if settings.DEBUG:
                ip = '178.92.248.224'
            request.LOCATION_DATA = g.city(ip)



