from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to, direct_to_template
from django.template.context import RequestContext

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
GOOGLE_MAPS_API_KEY = getattr(settings, 'GOOGLE_MAPS_API_KEY','')
urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'index.html',  'extra_context': { 
                                    'GOOGLE_MAPS_API_KEY':GOOGLE_MAPS_API_KEY,
                                    } 
                                    }
        ),
    # url(r'^timemap/', include('timemap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', './media')
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                            (r'^plugin.js$', redirect_to, {'url':'/media/js/plugin.js'}),
                            )
