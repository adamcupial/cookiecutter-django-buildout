#pylint: disable=all

# Third party modules
from django.conf import settings
from django.conf.urls import *

{% if cookiecutter.admin_engine == 'grappelli' or cookiecutter.admin_engine == 'default' %}
from django.contrib import admin
admin.autodiscover()
{% endif %}

urlpatterns = patterns('',
    {% if cookiecutter.admin_engine == 'grappelli' %}(r'^grappelli/', include('grappelli.urls')), {% endif %}
    {% if cookiecutter.admin_engine == 'grappelli' or cookiecutter.admin_engine == 'default' %}(r'^admin/', include(admin.site.urls)),{% endif %}
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),
    )
