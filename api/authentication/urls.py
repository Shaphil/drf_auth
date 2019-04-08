from django.urls import include, path
from rest_framework import routers

from .views import Default, UserViewSet, RegistrationView, LoginView, LogoutView


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('greet/', Default.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='registration'),
]
