from django.conf.urls import url, include

from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='login/')),
    url(r'^chat/$', RedirectView.as_view(url='global/')),
    url('register/', views.register, name='register'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
