from django.urls import include, path
from rest_framework import routers

from .views import Default, UserViewSet, RegistrationView, LoginView


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('greet/', Default.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='registration'),
]
