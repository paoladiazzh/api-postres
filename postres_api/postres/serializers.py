from rest_framework import serializers

class PostreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=100)
    sabor = serializers.CharField(max_length=50)
    tamanio = serializers.CharField(max_length=10)