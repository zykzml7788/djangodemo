#!/user/bin/env python
#coding=utf-8
'''
@project : mock
@author  : djcps
#@file   : serializers.py
#@ide    : PyCharm
#@time   : 2019-05-22 11:03:18
'''
# 序列化
from django.contrib.auth.models import User,Group
from  rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Group
        fields = "__all__"