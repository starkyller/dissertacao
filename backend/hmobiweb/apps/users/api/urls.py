from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import(
    CustomAuthToken,
    LogoutAPIView,
    PatientDetailAPIView,
)
app_name='users'


urlpatterns = [
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout" ),
    path("user-info/<slug:alias>/", PatientDetailAPIView.as_view(), name="user-info"),
]