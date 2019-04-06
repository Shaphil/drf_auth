from rest_framework import status, views
from rest_framework.response import Response


class Default(views.APIView):
    """
    Dummy view
    """

    def get(self, request, *args, **kwargs):
        message = {'message': 'Welcome to the Authentication API'}
        return Response(message, status=status.HTTP_200_OK)
