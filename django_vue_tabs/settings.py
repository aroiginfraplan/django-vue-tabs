from django.conf import settings


DJANGO_VUE_TABS_USE_VUE_JS = getattr(
    settings, 'DJANGO_VUE_TABS_USE_VUE_JS', 'django_vue_tabs/vue-2.6.11.min.js'
)

DJ_FIELD_FILEMANAGER_INSTALLED = 'dj_field_filemanager' in settings.INSTALLED_APPS
