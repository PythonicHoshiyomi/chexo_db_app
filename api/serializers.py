from rest_framework import serializers
from chexo_app.models import DojoList, MemberList

class DojoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DojoList
        fields = ['id',
                  'dojo_name',
                  'member_list']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberList
        fields = '__all__'