
from django.urls import path, include
from .views import *
from rest_framework import  routers

router = routers.DefaultRouter()
router.register(r'products',ProductViewset,basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('subscriber/',SubscriberView.as_view(), name='subscriber'),
    path('careers/',CareerView.as_view(), name='careers'),
]
