from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from project.api.api_auth.views import RegistrationView, RegistrationValidationView

app_name = 'auth'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/validate/', PasswordResetValidateView.as_view(), name='password_reset_validate'),
    path('registration/', RegistrationView.as_view(), name='register'),
    path('registration/validation/',RegistrationValidationView.as_view(), name='register_validate'),

    path('api-auth/', include('rest_framework.urls')),
]
