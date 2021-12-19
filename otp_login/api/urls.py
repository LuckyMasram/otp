from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login' ),
    path('verifyotp/', VerifyOTPView.as_view(), name='verifyotp'),
    path('customer/', CustomerProfileView.as_view(), name='customer'),
    path('profile/', ProfileUploadView.as_view(), name='profile'),
    path('booktrade/', BookTradesmanView.as_view(), name='booktrade'),
]