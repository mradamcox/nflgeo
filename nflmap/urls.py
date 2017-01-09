from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.team_list, name='team_list'),
    url(r'^(?P<code>[\w-]+)/$', views.team_page, name='team_page'),
]