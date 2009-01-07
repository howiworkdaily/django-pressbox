from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

from pressbox import urls as pressbox_urls
from pressbox.views import press_detail, press_list, press_regroup, press_with_templatetag

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url (
        regex = r'^press/$',
        view = press_list,
        name = 'press_list',
        ),
    url (
        regex = r'^press_regroup/$',
        view = press_regroup,
        name = 'press_regroup',
        ),
    url (
        regex = r'^press_bytag/$',
        view = press_with_templatetag,
        name = 'press_with_templatetag',
        ),
    url (
        regex = r'^press/(?P<slug>[-\w]+)/$',
        view = press_detail,
        name = 'press_detail',
        ),
    url (
        r'^$',
        direct_to_template,
        {'template': 'home.html'},
        name = 'home',
        ),
)

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

