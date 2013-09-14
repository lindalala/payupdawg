from django.conf.urls import patterns, include, url
from webapp.views import goHome

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^webapp/', include('webapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': '/Users/lindaxli/Desktop/PayUpDawg/'
                              'payupdawg/webapp/webapp/static/'}),

   url(r'^/?$', goHome),
)
