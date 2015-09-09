from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls'), name='comments'),
    url(r'^home$', views.home, name='home'),
    url(r'^categories$', views.categories,name='categories'),
    url(r'^teams$', views.teams, name='teams'),
    url(r'^tickets$', views.tickets, name='tickets'),
    url(r'^category/(?P<slug>[-\w\d]+)/$', views.category, name='category'),
    url(r'^category/(?P<slug>[-\w\d]+)/(?P<ticketSlug>[-\w\d]+)/$', views.viewTicket, name='viewTicket'),
    url(r'^newUser/$', views.newUser, name = 'newUser'),
    url(r'^login/$', views.userLogin, name='login'),
    url(r'^logout/$', views.userLogout, name='logout'),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {'document_root': settings.MEDIA_ROOT}), )