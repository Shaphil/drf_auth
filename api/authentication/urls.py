from django.urls import include, path
from rest_framework import routers

from .views import Default, UserViewSet, RegistrationView


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('greet/', Default.as_view()),
    path('register/', RegistrationView.as_view(), name='registration'),
]
