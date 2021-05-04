from django.db import models
from mongoengine import *
class Company1(DynamicDocument):
   cname=DictField(required=True)
   caddress=DictField()
   cphone=StringField()
   revenue=IntField()
   czoominfo=DictField()
   industry=StringField()

class Person1(DynamicDocument):
   pname=StringField(required=True)
   paddress=DictField()
   pphone=StringField()
   email=EmailField()
   title=StringField()
   pzoominfo=DictField()
   company=ReferenceField(Company1)


# Create your models here.
