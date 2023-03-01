from django.urls import path, include
from authentication import LoginView, SignupView, LogoutView

app_name = 'authentication'

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]