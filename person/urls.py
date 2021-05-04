from django.urls import path
from person.views import *
from django.conf.urls import url

urlpatterns = [
    path('personcreate/', PersonCreateView.as_view(), name='person-list'),
    path('personupdate/<str:pk>', PersonRetrieveUpdateDestroyView.as_view(), name='person-update'),
]