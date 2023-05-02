from django.urls import path
from auth2.views import register, _login, home, _logout,profile,reset_password,verify
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login2/', LoginView.as_view(), name='login2'),
    path('logout2/', LogoutView.as_view(), name='logout_2'),

    path('', register, name='register'),
    path('login/', _login, name='login'),
    path('home/', home, name='home'),
    path('logout/', _logout, name='logout'),

    path('profile/', profile, name='profile'),
    path('reset_password/', reset_password, name='reset_password'),
    path('verify/', verify, name='verify'),
]
