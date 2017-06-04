from django.conf.urls import url

from . import views

app_name = 'shops'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<shop_id>[0-9]+)/$', views.detail, name='detail'),
]
