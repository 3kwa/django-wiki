from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiki.views.home', name='home'),
    # url(r'^wiki/', include('wiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^wiki/$', 'wiki.views.index'),
    url(r'^wiki/log/$', 'wiki.views.log'),
    url(r'^wiki/(?P<title>.+)/edit/$', 'wiki.views.edit'),
    url(r'^wiki/(?P<title>.+)/save/$', 'wiki.views.save'),
    url(r'^wiki/(?P<title>.+)/log/$', 'wiki.views.log'),
    url(r'^wiki/(?P<title>.+)/$', 'wiki.views.page'),
)
