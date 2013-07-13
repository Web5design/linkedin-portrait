from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portrait.views.home', name='home'),
    url(r'^home', 'portrait.views.home', name='home'),
    url(r'^auth', 'portrait.views.auth', name='auth'),
)
