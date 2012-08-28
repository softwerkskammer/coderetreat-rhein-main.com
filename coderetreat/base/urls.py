# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from coderetreat import settings

urlpatterns = patterns('',
    url(r"^$", TemplateView.as_view(template_name="home.html"),
        name="home"),
    url(r"^learnmore$", TemplateView.as_view(template_name="learnmore.html"),
        name="learnmore"),
    url(r"^imprint$", TemplateView.as_view(template_name="imprint.html"),
            name="imprint"),
    url(r"^dec-2011$", TemplateView.as_view(template_name="legacy/dec-2011.html"),
            name="dec-2011"),
    url(r"^dec-2011/what-is-a-coderetreat$", 
            TemplateView.as_view(template_name="legacy/what-is-coderetreat.html"),
            name="dec-2011-what-is-a-coderetreat"),
    url(r"^mar-2012$", TemplateView.as_view(template_name="legacy/mar-2012.html"),
            name="mar-2012"),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)