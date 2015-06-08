from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ticket_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', views.home, name='home'),
    url(r'^categories$', views.categories,name='categories'),
    url(r'^teams$', views.teams, name= 'teams'),
    url(r'^tickets$', views.tickets, name= 'tickets'),
    url(r'^category/(?P<slug>[-\w\d]+)/$', views.category, name='category'),
    url(r'^category/(?P<slug>[-\w\d]+)/(?P<ticketSlug>[-\w\d]+)/$', views.viewTicket, name='viewTicket'),

    )