DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'quester',
        'USER': 'postgres',
        'PASSWORD': '111',
        'HOST': 'localhost',
    }
}


# LOCAL_INSTALLED_APPS = (
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # Uncomment the next line to enable the admin:
#     # 'django.contrib.admin',
#     # Uncomment the next line to enable admin documentation:
#     # 'django.contrib.admindocs',
# )