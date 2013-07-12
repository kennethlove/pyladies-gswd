from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^blog/', include('posts.urls', namespace='posts')),
    url(r'^admin/', include(admin.site.urls)),
    ('^pages/', include('django.contrib.flatpages.urls')),
)
