from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import(
    CustomAuthToken,
    PatientDetailAPIView,
)
app_name='users'


urlpatterns = [
    path("login", CustomAuthToken.as_view(), name="login"),
    path("user-info/<uuid:alias>", PatientDetailAPIView.as_view(), name="user-info"),
]