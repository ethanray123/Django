from . import views
from django.urls import re_path

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]