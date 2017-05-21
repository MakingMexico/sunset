from django.conf.urls import url
from buildings.views import *

urlpatterns = [

    url(r'^upload_building/$',
        CreateBuilding.as_view(),
        name='new_building'),

]
