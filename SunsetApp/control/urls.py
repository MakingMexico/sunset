from django.conf.urls import url
from control.views import *

urlpatterns = [

    url(r'^$',
        IndexView.as_view(),
        name='index'),

    url(r'^user_buildings',
        HomeView.as_view(),
        name='home'),

]
