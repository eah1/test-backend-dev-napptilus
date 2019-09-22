from rest_framework import serializers
from .models import OompaLoompa


class OompaLoompaSerializer(serializers.ModelSerializer):

    class Meta:

        model = OompaLoompa
        fields = ('name', 'age', 'job')


class OompaLoompaCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = OompaLoompa
        fields = '__all__'
