from django.urls import path
from .views import SignUpView, LoginView, profile_view


# account' a ait login, signup ve kullanıcı proflini belirten url' ler tanımlanır.
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
]
