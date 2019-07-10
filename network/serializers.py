from rest_framework import serializers


class PeerSerializer(serializers.Serializer):
    peer = serializers.CharField()
