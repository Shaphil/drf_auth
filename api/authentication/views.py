from rest_framework import status, views, viewsets
from rest_framework.response import Response

from .models import Token, User
from .serializers import UserSerializer


class Default(views.APIView):
    """
    Dummy view
    """

    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        message = {'message': 'Welcome to the Authentication API'}
        return Response(message, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationView(views.APIView):
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        required_fields = ('username', 'email', 'password')
        for field in required_fields:
            if field not in request.data:
                return Response(
                    {'error': 'This field is required {}'.format(field)},
                    status=status.HTTP_400_BAD_REQUEST
                )

        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            user = User(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
            user.save()

            return Response({'Message': 'User created'}, status=status.HTTP_201_CREATED)

        return Response({'Error': 'Username already taken'}, status=status.HTTP_409_CONFLICT)


class LoginView(views.APIView):
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        required_fields = ('username', 'password')
        for field in required_fields:
            if field not in request.data:
                return Response(
                    {'error': 'This field is required {}'.format(field)},
                    status=status.HTTP_400_BAD_REQUEST
                )

        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            return Response({'Error': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)

        is_correct_password = user.check_password(request.data['password'])
        if is_correct_password:
            token, created = Token.objects.get_or_create(user_id=user.id)
            return Response({'Token': token.key}, status=status.HTTP_202_ACCEPTED)

        return Response({'Error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):

    def post(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=status.HTTP_200_OK)
