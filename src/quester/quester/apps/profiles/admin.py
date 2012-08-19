from django.contrib.gis import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
