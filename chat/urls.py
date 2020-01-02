from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [
    url(r'^login/$',views.login, name='login'),
    url(r'^process/$',views.processdata, name ='process'),
    url(r'^show/$',views.show, name = 'shows'),
    url(r'^logout/$',views.logout, name = 'logout'),
    url(r'^show/(?P<user_id1>[0-9]+)/(?P<user_id2>[0-9]+)/messages/$',views.messages, name = "message")
]

