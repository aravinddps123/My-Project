
from .models import SchemaItem

from rest_framework import serializers

class SchemaSerializer(serializers.ModelSerializer):

    schemafile  = serializers.FileField(max_length=None, use_url=True)


    class Meta:

        model = SchemaItem
        fields = ['user','schemaname', 'changelog', 'schemafile']

        read_only_fields =['user']