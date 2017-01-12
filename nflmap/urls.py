from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.team_list, name='team_list'),
    url(r'^$', views.index, name='index'),
    url(r'^team/(?P<code>[\w-]+)/$', views.team_page, name='team_page'),
    url(r'^json/(?P<code>[\w-]+)/$', views.get_colleges_json, name='college_json'),
    
    
]