import os
from itertools import count
from rest_framework.serializers import *
from django.contrib.auth.models import *
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import *
from django.db.models import *
# from rest_framework_mongoengine.serializers import *
# from renter.models import MyModel1

# from classification_list.models import MyModel2
# import renter.models as renter_models
# import from classification_list.models as classification_models *
# from django.contrib.gis.db import models

from rest_framework import serializers
from rest_framework_mongoengine import serializers
from rest_framework.relations import HyperlinkedRelatedField
# from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from django.contrib.auth.models import User, Group
# from mongoengine.django.shortcuts import *
import mongoengine
from person.models import *
class CompanySerializer(serializers.DocumentSerializer):
    class Meta:
        model=Company1

class PersonSerializer(serializers.DocumentSerializer):

    company = CompanySerializer(many=False)

    class Meta:
        model = Person1
        fields = ['pname', 'paddress','pphone','email','title','pzoominfo','company']
    def create(self, validated_data):
        company = validated_data.pop('company')
        # company_cname=validated_data.pop(company["cname"])
        print(company['cname']['name1'])
        print(company)
        czid=company['czoominfo']['czoomid']
        person = Person1.objects.create(**validated_data)
        czid_count=Company1.objects.filter(czoominfo__czoomid=czid).count()
        czid_count_first = Company1.objects.filter(czoominfo__czoomid=czid).first()
        print(czid_count)
        # print("name:",czid_count_first.cname)
        # print("ref:",czid_count_first.to_dbref)

        if(czid_count==0):

            c=Company1.objects.create(**company)
            person.company = []

            print("aa")
            c.save()
            person.company = c.to_dbref()
        else:
            person.company = czid_count_first.to_dbref()
        person.save()
        print(person.company)
        return person
    def update(self, instance, validated_data):
        print("vd",validated_data)
        # ['pname', 'paddress', 'pphone', 'email', 'title', 'pzoominfo', 'company']
        company = validated_data.get('company',None)

        # instance.author=validated_data.pop('author')
        # print("auth::",instance.author)
        instance.pname = validated_data.get('pname',instance.pname)
        instance.to_dbref = validated_data.get('to_dbref', instance.to_dbref)
        instance.paddress = validated_data.get('paddress',instance.paddress)
        instance.pphone = validated_data.get('pphone',instance.pphone)
        instance.email = validated_data.get('email',instance.email)
        instance.title = validated_data.get('title',instance.title)
        instance.pzoominfo = validated_data.get('title',instance.pzoominfo)
        # instance.name = validated_data['author_name']

        # print("aname::",author['name'])
        # auth_rate=Person.objects.filter(author__name=instance.name).aggregate(Total=Sum('rating'))
        company_cnt = Company1.objects.filter(to_dbref=instance.to_dbref).count()
        company_first = Company1.objects.filter(czoominfo__czoomid=instance.to_dbref).first()
        print("ar:::", company_cnt)
        # if()
        # if(com[company_cnt == 1):
        #     auth_rate['Total']=0
        # tot_rat=instance.rating+auth_rate['Total']
        # print("ar:::",auth_rate['Total'])
        # auth_avg=tot_rat/(auth_cnt+1)
        # print("aavg::",auth_avg)
        if (company_cnt == 0):

            c = Company1.objects.create(**company)
            instance.company = []

            print("aa")
            c.save()
            instance.company = c.to_dbref()
        else:
            instance.company = company_first.to_dbref()
        instance.save()
        return instance
        # if(author is not None):
        #     author_id, created = Author.objects.get_or_create(name=author['name'], age=author['age'])
        #     author_id.auth_rate = auth_avg
        #     author_id.save()
        #     instance.author_id=author_id.id
        #     print("autid::",author_id.id)
        #     # if(author_id.id>0):
        #     print("aid::",author_id)
        # # author_id.save()
        # # author_id.auth_rate = auth_avg
        # instance.save()
        # return instance
# def save(self):
#     super(BookSerializer, self).save()

# class UserProfileSerializer(MongoEngineModelSerializer):
#     friends = PublicProfileSerializer(many=True, allow_add_remove=True)
#
#     class Meta:
#         model = UserProfile
#         depth = 1
#         exclude = ('db_id',)
#
#
# class PublicProfileSerializer(MongoEngineModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('first_name', 'last_name', 'id')
#
#     def update(self, user_profile_instance, validated_friend_data):
#         user_profile_instance.friends.extend(validated_friend_data)
#         user_profile_instance.save()
#         return user_profile_instance