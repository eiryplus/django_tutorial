from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
]
