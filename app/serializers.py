from rest_framework import serializers
from .models import Bag


class BagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = ('pk', 'country', 'city', 'location',
                  'uploader', 'vehicle', 'date', 'description', 'start', 'end')
