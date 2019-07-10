from rest_framework import (
    status, views
)
from rest_framework.response import Response

from .serializers import PeerSerializer


class PeerView(views.APIView):
    def post(self, request):
        serializer = PeerSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data['peer'])

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
