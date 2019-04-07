from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from .models import Token, User


class TokenBasedAuthentication(BaseAuthentication):
    def authenticate(self, request):
        header = get_authorization_header(request)

        if header is None:
            return None

        token = header.split()
        if len(token) == 0:
            raise AuthenticationFailed('Authentication token not provided')
        elif len(token) != 2:
            raise AuthenticationFailed(
                'Authentication header must contain two space separated values'
            )

        token_key = token[1].decode('utf-8')
        return self.get_token_user(token_key)

    def get_token_user(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid credentials')

        return (token.user, key)
