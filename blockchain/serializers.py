from rest_framework import serializers


class BlockSerializer(serializers.Serializer):
    index = serializers.IntegerField(required=False)
    data = serializers.CharField()
    difficulty = serializers.IntegerField()
    nonce = serializers.IntegerField()
    timestamp = serializers.IntegerField(required=False)
    previous_block_hash = serializers.CharField(required=False)
    hash = serializers.CharField(required=False)
