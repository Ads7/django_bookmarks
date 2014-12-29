import os.path
from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmarks.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import * 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root': settings.MEDIA_ROOT }),
    (r'^register/$', register_page),
    (r'^register/success/$', TemplateView.as_view(template_name= 'registration/register_success.html')),
    url(r'^admin/', include(admin.site.urls)),
)
