from django.urls import path

from .views import Default


urlpatterns = [
    path('', Default.as_view()),
]
