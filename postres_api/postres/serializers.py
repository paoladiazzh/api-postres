from rest_framework import serializers
from .models import Postre

class PostreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postre
        fields = '__all__'