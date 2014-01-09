from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    # the DetailView generic view (see views.py) requires the key value
    # captured from the URL to be called "pk"
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    
    # ex: /polls/5/results/
    # the DetailView generic view (see views.py) requires the key value
    # captured from the URL to be called "pk"
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)