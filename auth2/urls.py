from django.urls import path
from auth2.views import register

urlpatterns = [
    path('', register, name='register')
]
