from rest_framework import serializers
from .models import Dojo, Member

class DojoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dojo
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'