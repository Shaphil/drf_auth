from rest_framework import status, views, viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class Default(views.APIView):
    """
    Dummy view
    """

    def get(self, request, *args, **kwargs):
        message = {'message': 'Welcome to the Authentication API'}
        return Response(message, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
