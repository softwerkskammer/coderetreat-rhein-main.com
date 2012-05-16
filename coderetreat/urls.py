# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from coderetreat import settings

urlpatterns = patterns('',
    url(r"", include("coderetreat.base.urls"))
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )