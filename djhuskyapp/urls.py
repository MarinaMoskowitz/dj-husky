from django.conf.urls import url
from djhuskyapp import views

urlpatterns = [
    url(r'^party/$', views.party_list),
    url(r'^party/(?P<pk>[0-9]+)/$', views.party_detail),
    url(r'^song/$', views.song_list),
    url(r'^song/(?P<pk>[0-9]+)/$', views.song_detail),
]
