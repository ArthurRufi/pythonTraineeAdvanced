from django.urls import path
from .views import ViewMainAuth


urlpatterns = [
    path('login/', ViewMainAuth, name='login')
]
