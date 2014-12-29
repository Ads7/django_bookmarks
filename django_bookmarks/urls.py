from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmarks.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
)
