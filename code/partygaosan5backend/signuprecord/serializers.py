from rest_framework import serializers
from .models import PartyName

class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartyName
        fields = ['name','telephone']