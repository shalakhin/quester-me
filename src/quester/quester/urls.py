from django.conf.urls import patterns, include, url

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'quester.views.home', name='home'),
    # url(r'^quester/', include('quester.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'defaults.views.home', name='home'),
    url(r'^logout/$', 'defaults.views.logout', name='logout-page'),
    url(r'', include('social_auth.urls')),
)
