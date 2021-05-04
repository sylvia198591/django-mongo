from django.shortcuts import render
from mongoengine import *
# from django_mongo.settings import a
from person.serializers import *
from person.models import *
from rest_framework import permissions
from rest_framework.decorators import api_view
# from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.reverse import reverse
from person.serializers import *

from rest_framework import filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.generics import *
from UserLog.views import *
from pymongo import read_preferences
a=connect('project')
# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000
class PersonCreateView(ListCreateAPIView):
    serializer_class = PersonSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        # last_two_days = now() - timedelta(days=2)
        return Person1.objects.all()
class PersonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # lookup_field = 'to_dbref'
    queryset = Person1.objects.all()
    # serializer_class = BookSerializer
    # serializer_class1=BookSerializer1
    serializer_class = PersonSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser]
