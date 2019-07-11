from rest_framework import serializers


class PeerSerializer(serializers.Serializer):
    uri = serializers.CharField()
