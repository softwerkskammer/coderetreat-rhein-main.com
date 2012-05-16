# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r"^$", TemplateView.as_view(template_name="home.html"),
        name="home"),
    url(r"^learnmore$", TemplateView.as_view(template_name="learnmore.html"),
        name="learnmore"),
    url(r"^imprint", TemplateView.as_view(template_name="imprint.html"),
            name="imprint"),
)
