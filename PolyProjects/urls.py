from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('listings.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/listings/'}),
    url(r'^register/$', 'listings.views.register'),
    url(r'^verify_email/$', 'listings.views.verify_email'),
    url(r'^about/$', 'listings.views.about'),
    url(r'^calendar/$', 'listings.views.calendar'),
    url(r'^contact/$', 'listings.views.contact'),
    url(r'^faq/$', 'listings.views.faq'),
    url(r'^resources/$', 'listings.views.resources'),
)
