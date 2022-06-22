from rest_framework import serializers
from .models import Moviedata

class MovieSerializers(serializers.ModelSerializer):

    image  = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        """docstring for meta."""
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
        
