from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list_view, name='list'),
    url(r'^read/(?P<slug>[-\w]+)/$', views.post_detail_view, name='detail'),
)
