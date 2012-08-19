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
    url(r'^ajax/get_user_location', 'defaults.views.get_user_location', name='get_user_location'),
    url(r'^ajax/set_user_location', 'defaults.views.set_user_location', name='set_user_location'),
    url(r'^ajax/nearest_quests', 'quest.views.nearest_quests', name='nearest_quests'),
    url(r'^ajax/quest_form', 'quest.views.quest_form', name='quest_form'),
    url(r'^ajax/marker_fullinfo', 'quest.views.marker_fullinfo', name='marker_fullinfo'),
)
