from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.api.serializers import UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_OK, data='algo fallo')