from django.conf.urls import patterns, include, url
from cinema_times import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cinema_times.views.home', name='home'),
    url(r'^import/cineworld/cinemas/?', 'cinema_times.views.import_cineworld_schedule', name='import_cineworld_schedule'),
    url(r'^import/cineworld/schedule/?', 'cinema_times.views.import_cineworld_schedule', name='import_cineworld_schedule'),
    url(r'^locations/?$', 'cinema_times.views.cinema_locations', name='cinema_locations'),
    # url(r'^cinema_times/', include('cinema_times.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

