from django.conf.urls import patterns, url

from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='tasks/tasks.html')),
    url(r'^index', TemplateView.as_view(template_name='tasks/index.html')),
    url(r'^video', TemplateView.as_view(template_name='tasks/video.html'))
)
