from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^add$', views.add),
    url(r'^addfavorite/(?P<id>\d+)$', views.addfavorite),
    url(r'^remove/(?P<id>\d+)$', views.remove),
     url(r'^show/(?P<id>\d+)$', views.show),

]
