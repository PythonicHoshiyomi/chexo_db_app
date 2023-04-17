from rest_framework import serializers
from chexo_app.models import DojoList, MemberList

class DojoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DojoList
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberList
        fields = '__all__'